#!/usr/bin/env python3
from pathlib import Path
import json, re, sys, hashlib

ROOT=Path(__file__).resolve().parents[1]
F=ROOT/'evaluation'/'fixtures'
errors=[]; summary=[]

def get_json_path(obj, path):
    cur=obj
    for part in path.split('.'):
        if isinstance(cur,list): cur=cur[int(part)]
        else: cur=cur[part]
    return cur

def run_check(root,c):
    p=root/c.get('file','') if c.get('file') else root
    typ=c['type']
    try:
        if typ=='file_exists': return p.exists()
        if typ in ('contains','not_contains','regex','regex_absent','count_min','count_max'):
            s=p.read_text(encoding='utf-8')
            if typ=='contains': return c['value'] in s
            if typ=='not_contains': return c['value'] not in s
            if typ=='regex': return re.search(c['pattern'],s,re.M|re.S) is not None
            if typ=='regex_absent': return re.search(c['pattern'],s,re.M|re.S) is None
            n=s.count(c['value'])
            return n>=c['count'] if typ=='count_min' else n<=c['count']
        if typ=='json_equals':
            obj=json.loads(p.read_text(encoding='utf-8'))
            return get_json_path(obj,c['path'])==c['value']
    except Exception:
        return False
    return False

for fx in sorted(p for p in F.iterdir() if p.is_dir()):
    checks=fx/'checks.json'; base=fx/'baseline'; gold=fx/'golden'
    if not checks.exists() or not base.exists() or not gold.exists():
        errors.append(f'{fx.name}: missing checks/baseline/golden'); continue
    manifest_path=fx/'manifest.json'
    if not manifest_path.exists(): errors.append(f'{fx.name}: manifest.json missing')
    else:
        manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
        for state in ['baseline','golden']:
            for rel,expected in manifest.get(state,{}).items():
                fp=fx/state/rel
                if not fp.exists(): errors.append(f'{fx.name}: pinned file missing {state}/{rel}')
                else:
                    actual=hashlib.sha256(fp.read_bytes()).hexdigest()
                    if actual!=expected: errors.append(f'{fx.name}: hash mismatch {state}/{rel}')
    spec=json.loads(checks.read_text(encoding='utf-8'))
    cs=spec.get('checks',[])
    if len(cs)<4: errors.append(f'{fx.name}: need >=4 executable checks')
    total=sum(c.get('weight',1) for c in cs)
    if total<50: errors.append(f'{fx.name}: machine check weight {total} < 50')
    bresults=[run_check(base,c) for c in cs]
    gresults=[run_check(gold,c) for c in cs]
    bscore=sum(c.get('weight',1) for c,ok in zip(cs,bresults) if ok)
    gscore=sum(c.get('weight',1) for c,ok in zip(cs,gresults) if ok)
    bfail=sum(1 for ok in bresults if not ok)
    if all(bresults): errors.append(f'{fx.name}: baseline unexpectedly passes every good-state check')
    if bfail<2: errors.append(f'{fx.name}: baseline only fails {bfail} checks; fixture too weak')
    if not all(gresults): errors.append(f'{fx.name}: golden does not pass all checks')
    summary.append({'id':fx.name,'baseline_score':bscore,'total':total,'baseline_failures':bfail,'golden_score':gscore,'golden_pass':all(gresults)})

print(json.dumps({'fixtures':summary,'errors':errors},indent=2))
sys.exit(1 if errors else 0)
