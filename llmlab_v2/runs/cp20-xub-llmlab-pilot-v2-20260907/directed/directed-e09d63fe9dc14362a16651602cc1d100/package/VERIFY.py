import hashlib, json, pathlib, re, sys, zipfile
def h(b): return hashlib.sha256(b).hexdigest()
def legacy_findings(ledger):
    lines = ['# Directed task findings', '', 'Task: ' + ledger['task_id'], '']
    for claim in ledger['claims']:
        lines += [f"## {claim['claim_id']} — {claim['status']}", '', claim['statement'], '', 'Domain: ' + claim.get('domain', ''), '', 'First missing step: ' + str(claim.get('first_missing_step') or 'None'), '']
    lines += ['Downstream claims not established: ' + ', '.join(ledger.get('downstream_claims_not_established', [])), '']
    return '\n'.join(lines)

def _cell(value):
    return str(value).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('|', '&#124;').replace('\r', '').replace('\n', '<br>')

def findings(ledger):
    version = ledger.get('schema_version', '1.0')
    if version == '1.0' and ledger.get('authoritative') is not True:
        return legacy_findings(ledger)
    if version != '1.1' or ledger.get('authoritative') is not True:
        raise ValueError('Unsupported or non-authoritative consolidated ledger')
    claims = ledger['claims']
    ids = [claim['claim_id'] for claim in claims]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate authoritative claim id')
    claims = sorted(claims, key=lambda claim: claim['claim_id'])
    lines = ['# Directed task findings', '', 'Task: ' + _cell(ledger['task_id']), '',
             '| Claim | Status | Statement |', '| --- | --- | --- |']
    for claim in claims:
        lines.append('| ' + ' | '.join(_cell(claim[key]) for key in ('claim_id', 'status', 'statement')) + ' |')
    lines += ['', '## Supporting evidence', '',
              'Shared implementations and shared inputs limit independence. Agreement is not a proof certificate; conflicting evidence requires review, never a vote.', '']
    for claim in claims:
        lines += ['- **' + _cell(claim['claim_id']) + '**: domain ' + _cell(claim.get('domain', '')) +
                  '; first missing step: ' + _cell(claim.get('first_missing_step') or 'None') + '.']
        evidence = claim.get('supporting_evidence', [])
        if not isinstance(evidence, list):
            raise ValueError('Supporting evidence must be a list')
        for item in sorted(evidence, key=lambda value: (value['lane_id'], value.get('status', ''))):
            files = item.get('evidence_files', [])
            if not isinstance(files, list):
                raise ValueError('Evidence files must be a list')
            lines += ['  - Lane ' + _cell(item['lane_id']) + ': ' + _cell(item['status']) +
                      '; independence: ' + _cell(item.get('independence_level', 'NOT_INDEPENDENT')) +
                      '; files: ' + ', '.join(_cell(path) for path in sorted(files)) + '.']
        if not evidence:
            lines += ['  - No supporting lane evidence recorded.']
    lines += ['', 'Downstream claims not established: ' + ', '.join(_cell(item) for item in ledger.get('downstream_claims_not_established', [])), '']
    return '\n'.join(lines)

def verify(root):
    root = pathlib.Path(root)
    excluded = {'FINAL_SHA256SUMS.txt', 'COMPLETE_PACKAGE.zip', 'PACKAGE_SHA256.txt'}
    for p in root.rglob('*'):
        if p.is_symlink(): raise ValueError('symlink rejected')
        name = p.relative_to(root).as_posix()
        if any(part.startswith('.') for part in pathlib.PurePosixPath(name).parts) or ':' in name or '\\' in name: raise ValueError('unsafe member')
        if any(re.search(r'(?i)(^|[_.-])(env|secret|credentials|authorization|token|private.?key)([_.-]|$)', part) for part in pathlib.PurePosixPath(name).parts): raise ValueError('secret filename')
    for p in root.rglob("*"):
        if p.is_file() and p.relative_to(root).as_posix() not in excluded:
            text = p.read_bytes().decode("utf-8", errors="replace")
            if re.search('(?i)(?:api[_-]?key|password|client_secret|access_token|refresh_token|private_key)["\']?\\s*[=:]\\s*["\']?[^\\s"\',}]{8,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----', text): raise ValueError("secret content")
    listed = {}
    for line in (root/'FINAL_SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
        digest, name = line.split('  ', 1)
        if not re.fullmatch('[0-9a-f]{64}', digest) or name in listed or name in excluded or '..' in pathlib.PurePosixPath(name).parts or pathlib.PurePosixPath(name).is_absolute() or ':' in name or '\\' in name: raise ValueError('unsafe/duplicate manifest member')
        listed[name] = digest
    actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.relative_to(root).as_posix() not in excluded}
    if actual != set(listed): raise ValueError('manifest membership mismatch')
    for name, digest in listed.items():
        p = root/name
        if p.is_symlink() or h(p.read_bytes()) != digest: raise ValueError('source hash mismatch: '+name)
    if (root/'VERIFY_OUTPUT.txt').read_bytes() != b'PASS: source, ledger, contract and ZIP verified\n': raise ValueError('invalid verification receipt')
    ledger = json.loads((root/'CLAIM_LEDGER.json').read_text(encoding='utf-8'))
    if (root/'MASTER_FINDINGS.md').read_text(encoding='utf-8') != findings(ledger): raise ValueError('claim ledger/Markdown contradiction')
    if (root/'TASK_CONTRACT_SHA256.txt').read_text().strip() != h((root/'TASK_CONTRACT.json').read_bytes()): raise ValueError('contract hash mismatch')
    archive = root/'COMPLETE_PACKAGE.zip'
    if not archive.is_file(): raise ValueError('missing ZIP')
    if (root/'PACKAGE_SHA256.txt').read_text(encoding='utf-8') != h(archive.read_bytes()) + '  COMPLETE_PACKAGE.zip\n': raise ValueError('ZIP hash mismatch')
    if archive.exists():
        with zipfile.ZipFile(archive) as z:
            expected = actual | {'FINAL_SHA256SUMS.txt'}
            if len(z.namelist()) != len(set(z.namelist())) or set(z.namelist()) != expected: raise ValueError('ZIP membership mismatch')
            for name in expected:
                if z.read(name) != (root/name).read_bytes(): raise ValueError('ZIP/source mismatch: '+name)
    return True
if __name__ == '__main__':
    try:
        verify(pathlib.Path(__file__).parent)
        print('PASS: source, ledger, contract and ZIP verified')
    except Exception as e:
        print('FAIL: '+str(e)); sys.exit(1)
