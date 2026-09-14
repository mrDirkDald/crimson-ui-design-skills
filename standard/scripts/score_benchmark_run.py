#!/usr/bin/env python3
from pathlib import Path
import argparse, json, sys

ap=argparse.ArgumentParser()
ap.add_argument('machine_results')
ap.add_argument('manual_score')
args=ap.parse_args()
m=json.loads(Path(args.machine_results).read_text(encoding='utf-8'))
u=json.loads(Path(args.manual_score).read_text(encoding='utf-8'))

machine_total=m['total']; machine_score=m['score']
if machine_total <= 0: raise SystemExit('machine total must be >0')
machine_60=round(machine_score/machine_total*60,2)

manual_fields={'ux_workflow':15,'visual_design':10,'platform_fit':5,'evidence_quality':10}
manual=0; errors=[]
for k,maxv in manual_fields.items():
    v=u.get(k)
    if not isinstance(v,(int,float)) or not 0 <= v <= maxv: errors.append(f'{k} must be 0..{maxv}')
    else: manual += v

penalties=u.get('penalties',[])
penalty_map={'unresolved_blocker':1000,'unresolved_high':15,'functional_regression':20,'fabricated_runtime_pass':20,'major_scope_violation':15,'unnecessary_redesign_negative_control':10,'material_wrong_routing':10}
pen=sum(penalty_map.get(x,0) for x in penalties)
final=max(0, machine_60+manual-pen)
eligible='unresolved_blocker' not in penalties and not u.get('blockers',[])
out={'machine_raw':machine_score,'machine_total':machine_total,'machine_score_60':machine_60,'manual_score_40':manual,'penalty':pen,'final_score_100':final,'eligible':eligible,'errors':errors}
print(json.dumps(out,indent=2))
sys.exit(1 if errors else 0)
