#!/usr/bin/env python3
"""Generate the V3 reseal patches (launcher, config, contract) from the V2 Stage-0 sources.

Read-only on the repository: reads the three V2 files, derives the V3 variants by exact string
edits, and writes V3_STAGE1.patch / V3_CONFIG.patch / V3_CONTRACT.patch plus the derived V3 files
into this directory. No repository file is modified. No Stage-1 launcher is executed.
"""
import difflib, hashlib, json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
OUT = pathlib.Path(__file__).resolve().parent
TASK = 'CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2'
D = f'research_manager/results/{TASK}_STAGE0'
LAUNCHER = f'{D}/{TASK}_STAGE1.py'
CONFIG = f'{D}/{TASK}_CONFIG.json'
CONTRACT = f'{D}/{TASK}_STAGE1_EXECUTION_INTEGRITY_AND_OUTPUT_CONTRACT.md'
CONSUMED_V2_SEAL = '11456b7d6f673e5cab6079850731cbda70373b77e4e0f532089d6783fd16c78e'
BOUND = ['CURRENT_RESEARCH_STATE.json', 'START_HERE_CURRENT_HANDOFF.md']


def sha256(b): return hashlib.sha256(b).hexdigest()
def blob(b): return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()


def replace_once(text, old, new, label):
    if text.count(old) != 1:
        raise SystemExit(f'{label}: anchor not unique/found: {old[:60]!r}')
    return text.replace(old, new)


def udiff(path, old, new):
    lines = list(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
                                      fromfile='a/' + path, tofile='b/' + path, n=3))
    return f'diff --git a/{path} b/{path}\n' + ''.join(lines)


# ---------------- launcher ----------------
v2_launcher = (REPO / LAUNCHER).read_bytes().decode('utf-8')
assert '\r' not in v2_launcher
v3_launcher = v2_launcher
v3_launcher = replace_once(
    v3_launcher,
    " '06768aebd233c874fbb2103f3f3ccadca7db5ae76c7f5fb051ab982cf737012f',\n}\n",
    " '06768aebd233c874fbb2103f3f3ccadca7db5ae76c7f5fb051ab982cf737012f',\n"
    f" '{CONSUMED_V2_SEAL}',\n}}\n",
    'launcher BLOCKED')
v3_launcher = replace_once(
    v3_launcher,
    "    for path,blob in config['frozen_dependencies'].items():\n"
    "        try: got=git('rev-parse',f'{stage0_base}:{path}')\n"
    "        except Exception: fail('frozen dependency unreadable at Phase A: '+path)\n"
    "        if got!=blob: fail('frozen dependency blob mismatch at Phase A: '+path)\n",
    "    bound_paths=config.get('phase_a_bound_governance_files')\n"
    "    if not isinstance(bound_paths,list) or not bound_paths: fail('config missing phase_a_bound_governance_files')\n"
    "    for path in bound_paths:\n"
    "        if path in config['frozen_dependencies']: fail('frozen_dependencies must not list a Phase-A-bound governance file: '+path)\n"
    "    for path,blob in config['frozen_dependencies'].items():\n"
    "        try: got=git('rev-parse',f'{stage0_base}:{path}')\n"
    "        except Exception: fail('frozen dependency unreadable at Phase A: '+path)\n"
    "        if got!=blob: fail('frozen dependency blob mismatch at Phase A: '+path)\n"
    "    bound=auth.get('phase_a_governance_blobs')\n"
    "    if not isinstance(bound,dict): fail('authorization missing phase_a_governance_blobs object')\n"
    "    for path in bound_paths:\n"
    "        expected=bound.get(path)\n"
    "        if not (isinstance(expected,str) and len(expected)==40 and all(c in '0123456789abcdef' for c in expected)): fail('authorization phase_a_governance_blobs malformed: '+path)\n"
    "        try: got=git('rev-parse',f'{stage0_base}:{path}')\n"
    "        except Exception: fail('Phase-A governance file unreadable: '+path)\n"
    "        if got!=expected: fail('Phase-A governance blob mismatch: '+path)\n",
    'launcher governance binding')

# ---------------- contract ----------------
v2_contract = (REPO / CONTRACT).read_bytes().decode('utf-8')
assert '\r' not in v2_contract
v3_contract = v2_contract
v3_contract = replace_once(
    v3_contract,
    "- `stage = STAGE_1_AUTHORIZED_NOT_EXECUTED`\n\nThe authorization JSON MUST NOT be required to contain `authorization_commit_sha`",
    "- `stage = STAGE_1_AUTHORIZED_NOT_EXECUTED`\n"
    "- `phase_a_governance_blobs`: an object mapping each Phase-A-bound governance file named by the Stage-0 config "
    "(`CURRENT_RESEARCH_STATE.json`, `START_HERE_CURRENT_HANDOFF.md`) to its exact Git blob SHA-1 at `canonical_stage0_base_sha`. "
    "These blobs are recorded by the Phase-B integrator after Phase-A read-back; they cannot be known at seal time because Phase A rewrites those files.\n\n"
    "The authorization JSON MUST NOT be required to contain `authorization_commit_sha`",
    'contract auth fields')
v3_contract = replace_once(
    v3_contract,
    "11. the canonical Stage-0 load-bearing artifacts and contract at `canonical_stage0_base_sha` match the exact sealed Git blob IDs and SHA-256 hashes recorded by the Stage-0 config.\n",
    "11. the canonical Stage-0 load-bearing artifacts and contract at `canonical_stage0_base_sha` match the exact sealed Git blob IDs and SHA-256 hashes recorded by the Stage-0 config;\n"
    "12. every `frozen_dependencies` entry of the Stage-0 config (immutable scientific/closeout inputs only) is present unchanged at `canonical_stage0_base_sha`, and no `frozen_dependencies` entry names a Phase-A-bound governance file;\n"
    "13. every Phase-A-bound governance file named by the Stage-0 config (`phase_a_bound_governance_files`) has, at `canonical_stage0_base_sha`, exactly the Git blob SHA-1 recorded under `phase_a_governance_blobs` in the Phase-B authorization JSON.\n",
    'contract validation list')
v3_contract = replace_once(
    v3_contract,
    "No authorization JSON field is required to equal the commit SHA that contains the JSON.\n",
    "No authorization JSON field is required to equal the commit SHA that contains the JSON.\n\n"
    "## Frozen dependency semantics\n"
    "`frozen_dependencies` in the Stage-0 config binds immutable inputs (the canonical V1 Stage-0 scientific program files and the V1 closeout decision) "
    "by content-addressed Git blob, checked at `canonical_stage0_base_sha`. Live governance files that the Phase-A or Phase-B integrator rewrites "
    "(`CURRENT_RESEARCH_STATE.json`, `START_HERE_CURRENT_HANDOFF.md`) MUST NOT appear in `frozen_dependencies`: their Phase-A blob does not exist at seal time, "
    "so a seal-time blob for them is structurally guaranteed to mismatch at Phase A (the V2 defect of 2026-09-05). They are bound instead by `phase_a_governance_blobs` in the Phase-B authorization JSON.\n",
    'contract semantics section')
v3_contract = replace_once(
    v3_contract,
    "- V2 candidate `06768aebd233c874fbb2103f3f3ccadca7db5ae76c7f5fb051ab982cf737012f` with canonical-state-path mismatch.\n",
    "- V2 candidate `06768aebd233c874fbb2103f3f3ccadca7db5ae76c7f5fb051ab982cf737012f` with canonical-state-path mismatch;\n"
    f"- consumed V2 seal `{CONSUMED_V2_SEAL}` (once-only authorization consumed on 2026-09-05 by a real invocation that failed at the frozen-dependency check before any mathematics; frozen-dependency semantics defect).\n",
    'contract blocked list')

# ---------------- config ----------------
v2_config_bytes = (REPO / CONFIG).read_bytes()
cfg = json.loads(v2_config_bytes)
assert (json.dumps(cfg, indent=2, sort_keys=True) + '\n').encode() == v2_config_bytes, 'V2 config is not canonical json.dumps(indent=2,sort_keys)'
cfg['blocked_seal_blacklist'].append(CONSUMED_V2_SEAL)
for p in BOUND:
    assert p in cfg['frozen_dependencies']
    del cfg['frozen_dependencies'][p]
cfg['phase_a_bound_governance_files'] = list(BOUND)
cfg['frozen_dependencies_semantics'] = (
    'Immutable inputs only: each entry is a content-addressed Git blob that must be present unchanged at '
    'canonical_stage0_base_sha (Phase A). Files rewritten by the Phase-A or Phase-B integrator MUST NOT be listed here; '
    'they are bound at Phase B through authorization phase_a_governance_blobs.')
cfg['authorization_model']['phase_a_governance_binding'] = (
    'for every path in phase_a_bound_governance_files: authorization_json.phase_a_governance_blobs[path] == '
    'git rev-parse <canonical_stage0_base_sha>:<path>; recorded by the Phase-B integrator after Phase-A read-back')
cfg['future_authorization']['required_fields'].append('phase_a_governance_blobs')
cfg['future_authorization']['phase_a_governance_blobs_definition'] = (
    'object mapping each phase_a_bound_governance_files path to its 40-hex Git blob SHA-1 at canonical_stage0_base_sha; '
    'unknown at seal time; written only at Phase B')
cfg['dry_run_gate_cases'] = {
    'G1': 'correctly built Phase A/Phase B pair with V3 binding => PASS',
    'G2': 'Phase-A state blob differs from the blob bound in the authorization JSON => FAIL',
    'G3': 'authorization JSON lacks phase_a_governance_blobs (V2-style authorization) => FAIL',
    'G4': 'config frozen_dependencies re-lists CURRENT_RESEARCH_STATE.json (V2-style config) => FAIL before any blob comparison',
    'G5': 'a frozen SCIENTIFIC input (V1 Stage-0 DEFINITIONS.md) is altered inside Phase A => FAIL at the frozen-dependency check',
}
cfg['dry_run_gate_expected'] = {'G1': 'PASS', 'G2': 'FAIL', 'G3': 'FAIL', 'G4': 'FAIL', 'G5': 'FAIL'}
cfg['schema'] = f'{TASK}_STAGE0_CONFIG_TWO_COMMIT_AUTHORIZATION_STATEPATH_PHASE_A_GOVERNANCE_BINDING_V5'
# hashes of the patched launcher and contract
lb = v3_launcher.encode('utf-8'); cb = v3_contract.encode('utf-8')
cfg['canonical_stage0_artifacts'][LAUNCHER] = {'git_blob_sha1': blob(lb), 'sha256': sha256(lb)}
cfg['canonical_stage0_artifacts'][CONTRACT] = {'git_blob_sha1': blob(cb), 'sha256': sha256(cb)}
cfg['contract']['sha256'] = sha256(cb)
v3_config = json.dumps(cfg, indent=2, sort_keys=True) + '\n'

# ---------------- emit ----------------
(OUT / 'V3_STAGE1.patch').write_bytes(udiff(LAUNCHER, v2_launcher, v3_launcher).encode('utf-8'))
(OUT / 'V3_CONFIG.patch').write_bytes(udiff(CONFIG, v2_config_bytes.decode('utf-8'), v3_config).encode('utf-8'))
(OUT / 'V3_CONTRACT.patch').write_bytes(udiff(CONTRACT, v2_contract, v3_contract).encode('utf-8'))
der = OUT / 'derived_v3_files'; der.mkdir(exist_ok=True)
(der / f'{TASK}_STAGE1.py').write_bytes(lb)
(der / f'{TASK}_CONFIG.json').write_bytes(v3_config.encode('utf-8'))
(der / f'{TASK}_STAGE1_EXECUTION_INTEGRITY_AND_OUTPUT_CONTRACT.md').write_bytes(cb)
summary = {
    'v2_launcher_sha256': sha256(v2_launcher.encode()), 'v3_launcher_sha256': sha256(lb), 'v3_launcher_git_blob': blob(lb),
    'v2_contract_sha256': sha256(v2_contract.encode()), 'v3_contract_sha256': sha256(cb), 'v3_contract_git_blob': blob(cb),
    'v2_config_sha256': sha256(v2_config_bytes), 'v3_config_sha256': sha256(v3_config.encode()),
    'launcher_lines_v2': v2_launcher.count('\n'), 'launcher_lines_v3': v3_launcher.count('\n'),
}
(OUT / 'V3_PATCH_HASHES.json').write_bytes((json.dumps(summary, indent=2, sort_keys=True) + '\n').encode())
print(json.dumps(summary, indent=2))
