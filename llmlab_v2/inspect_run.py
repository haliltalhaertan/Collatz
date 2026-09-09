import json
import hashlib
import zipfile
from pathlib import Path

here = Path(__file__).resolve().parent
folders = sorted((here / 'runs/cp20-xub-llmlab-pilot-v2-20260907/directed').glob('directed-*'))
for folder in folders:
    runtime = json.loads((folder / 'runtime.json').read_text(encoding='utf-8'))
    usage = runtime.get('usage', {})
    summary = {k: runtime.get(k) for k in ('status', 'final_status', 'active_lanes', 'completed_lanes')}
    summary['usage'] = {k: usage.get(k) for k in ('calls', 'provider_cost_usd', 'provider_cost_complete', 'provider_cost_lower_bound_usd', 'provider_cost_upper_bound_usd', 'wall_seconds')}
    summary['lanes'] = {}
    for lane in sorted((folder / 'lanes').iterdir()):
        path = lane / 'RESULT.json'
        complete = path.exists()
        if not complete:
            path = lane / 'PARTIAL.json'
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding='utf-8'))
        item = {k: data.get(k) for k in ('status', 'first_missing_step', 'usage')}
        item['public_answer_characters'] = len(data.get('public_findings', '') or data.get('content', ''))
        item['provider_attempts'] = data.get('provider_attempts', [])
        if complete:
            item['public_findings'] = data.get('public_findings', '')
            item['claim_results'] = data.get('claim_results')
        summary['lanes'][lane.name] = item
    archive = folder / 'package/COMPLETE_PACKAGE.zip'
    if archive.exists():
        with zipfile.ZipFile(archive) as z:
            summary['zip'] = {'members': len(z.infolist()), 'crc_error': z.testzip(), 'sha256': hashlib.sha256(archive.read_bytes()).hexdigest(), 'bytes': archive.stat().st_size}
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if (here / 'RESULT.json').exists():
        (here / 'PUBLIC_REVIEW.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
