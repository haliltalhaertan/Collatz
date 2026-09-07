#!/usr/bin/env python3
"""DRY-RUN HARNESS FOR THE V3 INTEGRITY GATE (Phase-A governance binding).

What it does
  * `git clone --no-hardlinks <repo> <work>/clone`, removes the `origin` remote (no push is possible),
    and builds SYNTHETIC Phase-A / Phase-B commit pairs on throwaway branches inside that clone only.
  * Applies V3_STAGE1.patch / V3_CONFIG.patch / V3_CONTRACT.patch to a byte-exact copy of the accepted
    Phase-A Stage-0 directory (checked out from commit 34ac0db into the clone), re-runs the sealed static
    control-flow checker on the patched launcher, recomputes canonical_stage0_artifacts, builds a SYNTHETIC
    seal ZIP, and runs the PATCHED launcher's integrity gate against each synthetic pair.
  * Case G1 must PASS; G2/G3/G4/G5 must FAIL with the expected reason string.
    G5 tampers a frozen SCIENTIFIC input (V1 Stage-0 DEFINITIONS.md) inside Phase A.
  * Reproduces the V2 root cause with git plumbing only (rev-parse), never by executing the V2 launcher.

What it never does
  * It never touches the real repository worktree, branches, or remotes (all work is in the clone; the
    clone has no remote). It never executes the sealed V2 launcher, never uses the real seal or the real
    authorization tuple, and never emits T1 START (the launcher has no such path; the harness asserts it).
  * It grants no authorization. A Stage-1 run still requires a fresh manager transaction.

Usage
  python DRY_RUN_INTEGRITY_GATE.py --repo <repo root> --work <dir under Temp/claude> [--keep] [--report out.json]
"""
import argparse, datetime, hashlib, json, os, pathlib, re, shutil, subprocess, sys, zipfile

TASK = 'CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2'
D = f'research_manager/results/{TASK}_STAGE0'
LAUNCHER = f'{D}/{TASK}_STAGE1.py'
CONFIG = f'{D}/{TASK}_CONFIG.json'
CONTRACT = f'{D}/{TASK}_STAGE1_EXECUTION_INTEGRITY_AND_OUTPUT_CONTRACT.md'
MANIFEST = f'{D}/{TASK}_PRE_RUN_SHA256SUMS.txt'
STATIC_CHECK = f'{D}/{TASK}_STATIC_CONTROL_FLOW_CHECK.py'
STATIC_RESULTS = f'{D}/{TASK}_STATIC_CONTROL_FLOW_RESULTS.json'
AUTH = f'research_manager/decisions/{TASK}_STAGE1_AUTHORIZATION.json'
STATE = 'CURRENT_RESEARCH_STATE.json'
HANDOFF = 'START_HERE_CURRENT_HANDOFF.md'
SRC_BASE = '8d274095b0e1acbe1fad0a73ef6a5293364902fc'   # historical Stage-0 source base (launcher STAGE0_SOURCE)
REAL_PHASE_A = '34ac0dbeb8c0ae2fddab706680f1682412b00786'  # accepted real Phase A; used only as a byte source for the Stage-0 dir
V2_STATE_FROZEN_BLOB = '3ba90bbf9e91ddc600235a38a800db90b03a07e0'
HERE = pathlib.Path(__file__).resolve().parent
PATCHES = ['V3_STAGE1.patch', 'V3_CONFIG.patch', 'V3_CONTRACT.patch']


def sha256(b): return hashlib.sha256(b).hexdigest()
def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()


class Clone:
    def __init__(self, path): self.path = pathlib.Path(path)
    def git(self, *args, check=True, binary=False):
        p = subprocess.run(['git', *args], cwd=self.path, capture_output=True)
        if check and p.returncode != 0:
            raise RuntimeError(f'git {" ".join(args)} failed: {p.stderr.decode(errors="replace")}')
        return p.stdout if binary else p.stdout.decode('utf-8', errors='replace').strip()
    def read(self, rel): return (self.path / rel).read_bytes()
    def write(self, rel, data: bytes):
        p = self.path / rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(data)
    def blob_at(self, commit, rel): return self.git('rev-parse', f'{commit}:{rel}')


def rmtree_force(path):
    def _chmod_retry(func, p, _exc): os.chmod(p, 0o700); func(p)   # git pack files are read-only on Windows
    shutil.rmtree(path, onerror=_chmod_retry)


def make_clone(repo, work):
    work = pathlib.Path(work); work.mkdir(parents=True, exist_ok=True)
    cl = work / 'clone'
    if cl.exists(): rmtree_force(cl)
    # -c core.longpaths=true is written into the NEW repo's config and used for its checkout:
    # this repository's artifact filenames exceed the Windows MAX_PATH default under a deep work dir.
    subprocess.run(['git', 'clone', '-c', 'core.longpaths=true', '--no-hardlinks', '--quiet',
                    str(repo), str(cl)], check=True)
    c = Clone(cl)
    c.git('config', 'core.longpaths', 'true')
    c.git('remote', 'remove', 'origin')                     # no remote => no push possible
    c.git('config', 'user.name', 'B4 V3 dry-run harness')
    c.git('config', 'user.email', 'dryrun@invalid')
    c.git('config', 'commit.gpgsign', 'false')
    for sha in (SRC_BASE, REAL_PHASE_A): c.git('cat-file', '-e', f'{sha}^{{commit}}')
    assert c.git('remote') == '', 'clone still has a remote'
    return c


def load_state(c): return json.loads(c.read(STATE))
def dump_json(obj): return (json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + '\n').encode('utf-8')


def build_phase_a(c, name, *, v2_style_config=False, tamper_scientific=None):
    """Synthetic Phase A on top of SRC_BASE: accepted Stage-0 dir bytes + V3 patches + integrator rewrite of live files.

    tamper_scientific: relative path of a frozen scientific input to corrupt at Phase A (case G5)."""
    c.git('checkout', '-q', '-B', f'dryrun/{name}/phaseA', SRC_BASE)
    c.git('checkout', '-q', REAL_PHASE_A, '--', D)          # byte-exact accepted Stage-0 artifacts
    for p in PATCHES: c.git('apply', '--whitespace=nowarn', str(HERE / p))
    declared = json.loads((HERE / 'V3_PATCH_HASHES.json').read_text())
    assert sha256(c.read(LAUNCHER)) == declared['v3_launcher_sha256'], 'patched launcher != declared hash'
    assert sha256(c.read(CONTRACT)) == declared['v3_contract_sha256'], 'patched contract != declared hash'
    # re-run the sealed static control-flow checker on the PATCHED launcher (AST only; no launcher execution)
    r = subprocess.run([sys.executable, str(c.path / STATIC_CHECK)], cwd=c.path, capture_output=True, text=True)
    static_ok = r.returncode == 0 and 'STATIC CONTROL FLOW PASS' in r.stdout
    cfg = json.loads(c.read(CONFIG))
    if v2_style_config:                                     # G4: regress to V2 semantics (live state file frozen at seal time)
        cfg['frozen_dependencies'][STATE] = V2_STATE_FROZEN_BLOB
    # recompute canonical_stage0_artifacts exactly as a reseal would (content-addressed, commit-independent)
    # The repository sets `* text=auto eol=lf` in .gitattributes, so the SHA-256 the launcher sees
    # (`git show <commit>:<path>`, i.e. blob bytes) is NOT the SHA-256 of the working-tree file on
    # Windows. Recompute both identifiers from the blob git will actually serve.
    changed = []
    for rel, e in cfg['canonical_stage0_artifacts'].items():
        blob = c.git('hash-object', '-w', '--', rel)
        sh = sha256(c.git('cat-file', 'blob', blob, binary=True))
        if (blob, sh) != (e['git_blob_sha1'], e['sha256']):
            changed.append(rel.rsplit('/', 1)[-1]); cfg['canonical_stage0_artifacts'][rel] = {'git_blob_sha1': blob, 'sha256': sh}
    assert cfg['contract']['sha256'] == sha256(c.read(CONTRACT))
    c.write(CONFIG, (json.dumps(cfg, indent=2, sort_keys=True) + '\n').encode())
    # regenerate the seal manifest for the (patched) member set.
    # Six sealed members (the V2 scientific program documents) live only inside the real seal ZIP and are
    # not tracked in the repository tree; for a SYNTHETIC seal they are filled with deterministic placeholder
    # bytes. The launcher only cross-checks the CONFIG and CONTRACT members against on-disk files, so the
    # placeholders exercise exactly the same seal-integrity code path.
    members = [ln.split('  ', 1)[1] for ln in c.read(MANIFEST).decode().splitlines() if ln.strip()]
    mbytes, synthesized = {}, []
    for m in sorted(members):
        p = c.path / D / m
        if p.exists():
            mbytes[m] = p.read_bytes()
        else:
            synthesized.append(m)
            mbytes[m] = f'DRY-RUN SYNTHETIC SEAL MEMBER (not tracked in the repository tree): {m}\n'.encode()
    manifest = ''.join(f'{sha256(mbytes[m])}  {m}\n' for m in sorted(members))
    c.write(MANIFEST, manifest.encode())
    mbytes[MANIFEST.rsplit('/', 1)[-1]] = manifest.encode()
    # integrator rewrite of the two live governance files (this is what broke V2)
    st = load_state(c); st['active_task']['stage'] = 'STAGE_0_REPAIR_ACCEPTED_AWAITING_AUTHORIZATION'
    st['active_integrator'] = {'holder': f'dryrun-{name}', 'scope': 'synthetic', 'base_commit': SRC_BASE, 'acquired_at': utc(), 'status': 'HELD'}
    st['dry_run_marker'] = name
    c.write(STATE, dump_json(st))
    c.write(HANDOFF, c.read(HANDOFF) + f'\n<!-- dry-run Phase A rewrite {name} -->\n'.encode())
    add_paths = [D, STATE, HANDOFF]
    tampered_from = None
    if tamper_scientific:                                   # G5: corrupt a frozen SCIENTIFIC input inside Phase A
        tampered_from = c.blob_at(SRC_BASE, tamper_scientific)
        c.write(tamper_scientific, c.read(tamper_scientific) + b'\n<!-- dry-run scientific tamper -->\n')
        add_paths.append(tamper_scientific)
    c.git('add', '-A', '--', *add_paths)
    c.git('commit', '-q', '-m', f'DRYRUN Phase A ({name}) synthetic canonicalization')
    a_sha = c.git('rev-parse', 'HEAD')
    # synthetic seal ZIP (deterministic, sorted members, manifest last-by-name irrelevant: launcher requires sorted namelist)
    seal = c.path.parent / f'seal_{name}.zip'
    with zipfile.ZipFile(seal, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for m in sorted(mbytes):
            zi = zipfile.ZipInfo(m, date_time=(2026, 1, 1, 0, 0, 0)); zi.compress_type = zipfile.ZIP_DEFLATED; zi.create_system = 0
            z.writestr(zi, mbytes[m])
    info = {'phase_a': a_sha, 'seal': str(seal), 'seal_sha256': sha256(seal.read_bytes()),
            'synthetic_seal_members_not_in_repo_tree': synthesized,
            'contract_sha256': cfg['contract']['sha256'], 'config_sha256': sha256(c.read(CONFIG)),
            'static_control_flow_on_patched_launcher': 'PASS' if static_ok else 'FAIL',
            'canonical_artifact_entries_recomputed_differently_from_patch': changed,
            'state_blob_at_phase_a': c.blob_at(a_sha, STATE), 'handoff_blob_at_phase_a': c.blob_at(a_sha, HANDOFF),
            'v2_frozen_state_blob_would_match_at_phase_a': c.blob_at(a_sha, STATE) == V2_STATE_FROZEN_BLOB}
    if tamper_scientific:
        info['tampered_scientific_input'] = {'path': tamper_scientific, 'sealed_blob': tampered_from,
                                             'blob_at_phase_a': c.blob_at(a_sha, tamper_scientific)}
    return info


def build_phase_b(c, name, a_sha, info, *, base=None, omit_binding=False, bind_from=None):
    c.git('checkout', '-q', '-B', f'dryrun/{name}/phaseB', base or a_sha)
    bind_src = bind_from or a_sha
    auth = {'authorized_v2_seal_sha256': info['seal_sha256'], 'v2_contract_sha256': info['contract_sha256'],
            'canonical_stage0_base_sha': a_sha, 'stage': 'STAGE_1_AUTHORIZED_NOT_EXECUTED'}
    if not omit_binding:
        auth['phase_a_governance_blobs'] = {STATE: c.blob_at(bind_src, STATE), HANDOFF: c.blob_at(bind_src, HANDOFF)}
    c.write(AUTH, dump_json(auth))
    st = load_state(c); st['active_task']['stage'] = 'STAGE_1_AUTHORIZED_NOT_EXECUTED'; c.write(STATE, dump_json(st))
    c.git('add', '-A', '--', AUTH, STATE)
    c.git('commit', '-q', '-m', f'DRYRUN Phase B ({name}) synthetic authorization')
    return c.git('rev-parse', 'HEAD')


def run_gate(c, name, a_sha, b_sha, info):
    """Run the PATCHED launcher's integrity gate with a synthetic tuple. Returns observation dict."""
    c.git('checkout', '-q', f'dryrun/{name}/phaseB')
    out = f'{D}/{TASK}_STAGE1_RESULTS.json'
    argv = [sys.executable, str(c.path / LAUNCHER), '--config', CONFIG, '--seal', info['seal'],
            '--canonical-stage0-base-sha', a_sha, '--authorization-commit-sha', b_sha,
            '--authorized-seal-sha256', info['seal_sha256'], '--contract-sha256', info['contract_sha256'], '--output', out]
    p = subprocess.run(argv, cwd=c.path, capture_output=True, text=True)
    sd = c.path / D
    obs = {'exit_code': p.returncode, 'stdout': p.stdout.strip(), 'stderr_tail': p.stderr.strip()[-400:],
           'failure_record': None, 'witness_written': (sd / f'{TASK}_STAGE1_RUN_WITNESS.json').exists(),
           'gate_written': (sd / f'{TASK}_STAGE1_PRE_T1_GATE.json').exists(),
           'ledger_events': [], 'output_T1_T8': None, 't1_start_emitted': False}
    fr = sd / f'{TASK}_STAGE1_INPUT_INTEGRITY_FAILURE.json'
    if fr.exists(): obs['failure_record'] = json.loads(fr.read_text(encoding='utf-8'))
    lg = sd / f'{TASK}_STAGE1_EXECUTION_LEDGER.jsonl'
    if lg.exists():
        rows = [json.loads(x) for x in lg.read_text(encoding='utf-8').splitlines() if x.strip()]
        obs['ledger_events'] = [r.get('event') for r in rows]
        # A genuine T1 START event only; the legitimate 'PRE_T1_GATE' event also contains the
        # substring 'T1' and must not be mistaken for one (harness fix, 2026-09-07).
        obs['t1_start_emitted'] = any(re.fullmatch(r'T1[ _-]?START', str(r.get('event', '')).upper()) for r in rows)
    obs['t1_start_emitted'] = obs['t1_start_emitted'] or 'T1 START' in p.stdout.upper()
    op = c.path / out
    if op.exists(): obs['output_T1_T8'] = json.loads(op.read_text(encoding='utf-8')).get('T1_T8')
    # clean generated files so the next case sees an absent output set
    c.git('checkout', '-q', '--', '.'); c.git('clean', '-fdq', '--', D)
    return obs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', required=True); ap.add_argument('--work', required=True)
    ap.add_argument('--keep', action='store_true'); ap.add_argument('--report', default=None)
    a = ap.parse_args()
    repo = pathlib.Path(a.repo).resolve(); work = pathlib.Path(a.work).resolve()
    assert repo not in work.parents and work != repo, 'work dir must be outside the repository'
    for p in PATCHES + ['V3_PATCH_HASHES.json']: assert (HERE / p).exists(), f'missing {p}'
    report = {'schema': f'{TASK}_V3_INTEGRITY_GATE_DRY_RUN_V1', 'utc': utc(), 'repo': str(repo), 'work': str(work),
              'sealed_v2_launcher_executed': False, 'real_seal_used': False, 'real_authorization_tuple_used': False,
              'T1_T8_executed': False, 'authorization_granted_by_this_run': False, 'cases': {}}
    c = make_clone(repo, work)
    report['clone_head_before'] = c.git('rev-parse', 'HEAD'); report['clone_remotes'] = c.git('remote')

    # --- V2 root-cause reproduction by git plumbing only (no launcher execution) ---
    report['v2_root_cause_plumbing'] = {
        'config_v2_frozen_blob_for_state': V2_STATE_FROZEN_BLOB,
        'state_blob_at_src_base_8d27409': c.blob_at(SRC_BASE, STATE),
        'state_blob_at_real_phase_a_34ac0db': c.blob_at(REAL_PHASE_A, STATE),
        'v2_check_line81_would_fail_at_real_phase_a': c.blob_at(REAL_PHASE_A, STATE) != V2_STATE_FROZEN_BLOB}

    # --- G1: correct pair => PASS ---
    i1 = build_phase_a(c, 'G1'); a1 = i1['phase_a']; b1 = build_phase_b(c, 'G1', a1, i1)
    o1 = run_gate(c, 'G1', a1, b1, i1)
    g1_pass = o1['exit_code'] == 0 and 'PRE-T1 INTEGRITY GATE: PASS' in o1['stdout'] and o1['gate_written'] \
        and o1['ledger_events'] == ['PRE_T1_GATE'] and not o1['t1_start_emitted'] \
        and o1['output_T1_T8'] == {f'T{i}': 'NOT_EXECUTED' for i in range(1, 9)}
    report['cases']['G1'] = {'expected': 'PASS', 'observed': 'PASS' if g1_pass else 'FAIL', 'phase_a': a1, 'phase_b': b1, 'build': i1, 'run': o1}

    # --- G2: tampered Phase A (state file differs from the blob the authorization binds) => FAIL ---
    c.git('checkout', '-q', '-B', 'dryrun/G2/phaseA', a1)
    st = load_state(c); st['dry_run_marker'] = 'G2-tampered-after-binding'; c.write(STATE, dump_json(st))
    c.git('add', '--', STATE); c.git('commit', '-q', '-m', 'DRYRUN Phase A (G2) tampered state')
    a2 = c.git('rev-parse', 'HEAD')
    b2 = build_phase_b(c, 'G2', a2, i1, bind_from=a1)       # authorization still binds the G1 (untampered) blobs
    o2 = run_gate(c, 'G2', a2, b2, i1)
    exp2 = f'Phase-A governance blob mismatch: {STATE}'
    g2_ok = o2['exit_code'] != 0 and exp2 in o2['stderr_tail'] and o2['failure_record'] is not None and o2['failure_record'].get('reason') == exp2 \
        and not o2['gate_written'] and not o2['witness_written']
    report['cases']['G2'] = {'expected': 'FAIL', 'expected_reason': exp2, 'observed': 'FAIL' if o2['exit_code'] else 'PASS', 'matches_expectation': g2_ok,
                             'phase_a': a2, 'phase_b': b2, 'run': o2}

    # --- G3: V2-style authorization without the binding field => FAIL ---
    b3 = build_phase_b(c, 'G3', a1, i1, omit_binding=True)
    o3 = run_gate(c, 'G3', a1, b3, i1)
    exp3 = 'authorization missing phase_a_governance_blobs object'
    g3_ok = o3['exit_code'] != 0 and (o3['failure_record'] or {}).get('reason') == exp3 and not o3['gate_written']
    report['cases']['G3'] = {'expected': 'FAIL', 'expected_reason': exp3, 'observed': 'FAIL' if o3['exit_code'] else 'PASS', 'matches_expectation': g3_ok,
                             'phase_a': a1, 'phase_b': b3, 'run': o3}

    # --- G4: V2-style config (live state file listed in frozen_dependencies) => FAIL at the semantic guard ---
    i4 = build_phase_a(c, 'G4', v2_style_config=True); a4 = i4['phase_a']; b4 = build_phase_b(c, 'G4', a4, i4)
    o4 = run_gate(c, 'G4', a4, b4, i4)
    exp4 = f'frozen_dependencies must not list a Phase-A-bound governance file: {STATE}'
    g4_ok = o4['exit_code'] != 0 and (o4['failure_record'] or {}).get('reason') == exp4 and not o4['gate_written']
    report['cases']['G4'] = {'expected': 'FAIL', 'expected_reason': exp4, 'observed': 'FAIL' if o4['exit_code'] else 'PASS', 'matches_expectation': g4_ok,
                             'phase_a': a4, 'phase_b': b4, 'build': i4, 'run': o4}

    # --- G5: tampered SCIENTIFIC input frozen dependency at Phase A => FAIL at the frozen-dependency check ---
    sci = f'research_manager/results/{TASK.replace("_V2", "_V1")}_STAGE0/{TASK.replace("_V2", "_V1")}_DEFINITIONS.md'
    i5 = build_phase_a(c, 'G5', tamper_scientific=sci); a5 = i5['phase_a']; b5 = build_phase_b(c, 'G5', a5, i5)
    o5 = run_gate(c, 'G5', a5, b5, i5)
    exp5 = f'frozen dependency blob mismatch at Phase A: {sci}'
    g5_ok = o5['exit_code'] != 0 and (o5['failure_record'] or {}).get('reason') == exp5 \
        and not o5['gate_written'] and not o5['witness_written']
    report['cases']['G5'] = {'expected': 'FAIL', 'expected_reason': exp5, 'observed': 'FAIL' if o5['exit_code'] else 'PASS',
                             'matches_expectation': g5_ok, 'phase_a': a5, 'phase_b': b5, 'build': i5, 'run': o5}

    report['verdict'] = 'PASS' if (g1_pass and g2_ok and g3_ok and g4_ok and g5_ok) else 'FAIL'
    report['clone_branches'] = c.git('branch', '--list', 'dryrun/*').split()
    if a.report: pathlib.Path(a.report).write_bytes(dump_json(report))
    print(json.dumps({k: report[k] for k in ('verdict', 'v2_root_cause_plumbing')}, indent=2))
    for k, v in report['cases'].items():
        print(f"{k}: expected={v['expected']} observed={v['observed']} exit={v['run']['exit_code']} reason={(v['run']['failure_record'] or {}).get('reason')}")
    if not a.keep: rmtree_force(c.path)
    return 0 if report['verdict'] == 'PASS' else 1


if __name__ == '__main__': raise SystemExit(main())
