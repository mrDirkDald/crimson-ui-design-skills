#!/usr/bin/env python3
from pathlib import Path
import argparse,json,statistics,sys
from collections import defaultdict
from jsonschema import Draft202012Validator

ap=argparse.ArgumentParser()
ap.add_argument('runs_dir')
ap.add_argument('--candidate', required=True)
ap.add_argument('--baseline')
ap.add_argument('--out')
args=ap.parse_args()
root=Path(__file__).resolve().parents[1]
schema=json.loads((root/'evaluation/run.schema.json').read_text(encoding='utf-8'))
val=Draft202012Validator(schema)
runs=[]; errors=[]
for p in sorted(Path(args.runs_dir).glob('*.json')):
    try:d=json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'{p.name}: invalid JSON {e}'); continue
    es=list(val.iter_errors(d))
    if es:
        errors.extend(f'{p.name}: {e.message}' for e in es); continue
    runs.append(d)

def stats(version):
    rs=[r for r in runs if r['skill_version']==version]
    if not rs: return None
    scores=[r['final_score_100'] for r in rs]
    bycat=defaultdict(list); bybench=defaultdict(list)
    for r in rs:
        bycat[r['category']].append(r['final_score_100']); bybench[r['benchmark_id']].append(r['final_score_100'])
    return {
      'version':version,'runs':len(rs),'benchmarks':len(bybench),
      'mean':round(statistics.mean(scores),2),'median':round(statistics.median(scores),2),
      'min':min(scores),'max':max(scores),
      'category_means':{k:round(statistics.mean(v),2) for k,v in sorted(bycat.items())},
      'runs_per_benchmark':{k:len(v) for k,v in sorted(bybench.items())},
      'regressions':sum(r['regressions'] for r in rs),
      'scope_violations':sum(bool(r['scope_violation']) for r in rs),
      'fabricated_passes':sum(bool(r['fabricated_pass']) for r in rs),
      'blockers':sum(r.get('blockers',0) for r in rs),
      'eligible_runs':sum(bool(r['eligible']) for r in rs),
      'avg_tokens':round(statistics.mean(r['metrics']['tokens'] for r in rs),2),
      'avg_tool_calls':round(statistics.mean(r['metrics']['tool_calls'] for r in rs),2),
      'avg_elapsed_seconds':round(statistics.mean(r['metrics']['elapsed_seconds'] for r in rs),2),
    }

cand=stats(args.candidate); base=stats(args.baseline) if args.baseline else None
if cand is None: errors.append('No candidate runs found')
promote=False; reasons=[]
if cand:
    if cand['mean'] < 85: reasons.append('candidate mean <85')
    if cand['median'] < 85: reasons.append('candidate median <85')
    if cand['category_means'] and min(cand['category_means'].values()) < 75: reasons.append('a category mean <75')
    if cand['fabricated_passes'] != 0: reasons.append('fabricated PASS detected')
    if cand['blockers'] != 0: reasons.append('unresolved blocker(s)')
    if any(n < 3 for n in cand['runs_per_benchmark'].values()): reasons.append('fewer than 3 runs for at least one tested benchmark')
    if base:
        if cand['mean'] <= base['mean']: reasons.append('candidate mean does not beat baseline')
        if cand['regressions'] > base['regressions']: reasons.append('regression count worsened')
        if cand['scope_violations'] > base['scope_violations']: reasons.append('scope violations worsened')
    promote=not reasons
out={'candidate':cand,'baseline':base,'promote':promote,'reasons':reasons,'validation_errors':errors}
text=json.dumps(out,indent=2); print(text)
if args.out: Path(args.out).write_text(text,encoding='utf-8')
sys.exit(1 if errors else 0)
