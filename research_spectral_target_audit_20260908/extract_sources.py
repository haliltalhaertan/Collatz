"""Preserve exact source bytes used in this exploratory target audit."""
from pathlib import Path
import hashlib
import json
import zipfile

root = Path(__file__).resolve().parent
archive = root.parent/'Collatz_Research_Archive_CURRENT.zip'
wanted = {
    'CP20_TASK8B3_E0_INTERVAL_ANTICONCENTRATION_REPORT.md',
    'CP20_TASK8B3_E1_HIGH_CONDUCTOR_REQUIRED_DECAY.md',
    'CP20_TASK8B3_E0_EXACT_RECURSION_V2.md',
}
rows = []
with zipfile.ZipFile(archive) as z:
    for name in z.namelist():
        leaf = name.rsplit('/', 1)[-1]
        if leaf not in wanted:
            continue
        data = z.read(name)
        (root/leaf).write_bytes(data)
        rows.append(dict(member=name, file=leaf, sha256=hashlib.sha256(data).hexdigest()))
assert len(rows) == len(wanted)
(root/'SOURCE_PROVENANCE.json').write_text(json.dumps(dict(
    archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(), sources=rows
), ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print('Preserved', len(rows), 'source documents without modifying archive.')
