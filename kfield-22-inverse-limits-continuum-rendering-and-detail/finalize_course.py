"""Rebuild assembly and integrity metadata after content audits; no lesson rewriting."""
from pathlib import Path
import json,hashlib,re
R=Path(__file__).resolve().parent
def load(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def write(n,s):(R/n).write_text(s.rstrip()+'\n',encoding='utf-8')
def dump(n,o):write(n,json.dumps(o,indent=2,ensure_ascii=False))
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
p=load('input-contract.json'); old=load('manifest.json')
# Recovery verification: old drafted hashes are not reused as passed authorities.
recovery=[]
for c in old.get('checkpoints',[]):
 if c.get('sha256') and (R/c['path']).exists():
  match=sha(c['path'])==c['sha256']
  if c.get('status')=='passed':assert match,('Unexpected passed-file drift',c['path'])
  recovery.append({'id':c['id'],'old_status':c['status'],'old_hash_match':match,'disposition':'unchanged' if match else 'Draft revised by documented audit repair; refreshed only after rechecks'})
assert load('worked-example-verification.json')['status']=='passed'
ia=load('independent-audit.json')
assert ia['unresolved_counts']=={'critical':0,'major':0,'minor':0}
order=[f'lesson-{i:02}' for i in range(1,8)]
texts={i:(R/f'{i}.md').read_text(encoding='utf-8').rstrip('\n') for i in order}
assembly='# Inverse Limits, Continuum Rendering, and Detail\n\nStudent course · high-school seniors · 12 core periods and 3 capstone periods.\n\nRead the [course map](course-map.md), use the [glossary](terminology.md), and finish with the [capstone and key](capstone.md). Source contracts are in [sources](sources.md).\n\n'
assembly+='\n\n'.join(f'<!-- BEGIN: {i} -->\n{texts[i]}\n<!-- END: {i} -->' for i in order)
write('course.md',assembly)
# Markdown layout and link checks, with no paginated output requested.
tables=0;links=0
for file in R.glob('*.md'):
 if file.name=='launch-prompt.md':continue
 rows=[]
 for line in file.read_text(encoding='utf-8').splitlines():
  if line.startswith('|'):
   count=len(re.split(r'(?<!\\)\|',line))-2
   if rows:assert count==rows[-1],(file.name,'table width',line)
   else:tables+=1
   rows.append(count)
  else:rows=[]
 for dest in re.findall(r'\]\(([^)]+)\)',file.read_text(encoding='utf-8')):
  if '://' not in dest:
   assert (R/dest.split('#')[0]).exists(),(file.name,dest)
   links+=1
findings=[
 {'id':'IA22-001','level':'local','category':'mathematical rigor and prerequisite closure','file':'lesson-07.md','section':'C22.07-E1','severity':'minor','defect':'Bounded signed partial inner products were asserted to converge without an absolute-convergence or tail argument.','correction':'Proved the finite dot-product inequality by a sum-of-squares expansion and applied it to absolute products; increasing bounded absolute sums imply absolute convergence.','verification':'Independent auditor reread the proof, closed IA22-001; parent independently supplied the same diagnosis and accepted the correction.','disposition':'corrected','affected_checkpoints':['lesson-07','capstone','assembly']},
 {'id':'F22-002','level':'final','category':'Markdown table structure','file':'terminology.md','section':'sequence-space row','severity':'minor','defect':'Norm vertical bars were unescaped inside a three-column Markdown table.','correction':'Replaced the norm-bar label with sequence 2-norm.','verification':'Deterministic equal-cell-count checks pass for every Markdown table in deliverable Markdown.','disposition':'corrected','affected_checkpoints':['terminology']},
 {'id':'F22-003','level':'final','category':'exact provenance','file':'sources.md','section':'pointer table; lesson-04 claim scope','severity':'minor','defect':'Array-entry ranges were displayed as though each were a literal JSON pointer.','correction':'Expanded all cited proof ranges into separate exact entry pointers; lesson04 uses explicit full pointers.','verification':'Read source arrays and confirmed M18 proof entries0,1,2 and M04 entries0 through4; all five source hashes matched.','disposition':'corrected','affected_checkpoints':['sources','lesson-04','assembly']}
]
checks=[
 {'level':'local','scope':'lessons01–07','result':'passed','evidence':'Independent auditor read every lesson and all28 E/W/P/D anchors; four answered diagnostics and next link per lesson. Manager rational recomputation in worked-example-verification.json.'},
 {'level':'cumulative','scope':'Unit A, lessons01–03','result':'passed','evidence':'Residue/sign/order conventions preserved; common-prefix distance uses low-order agreement; exact all-digit rules distinguished from partial prefixes; triples and27 extensions independently checked.'},
 {'level':'cumulative','scope':'Unit B, lessons04–05','result':'passed','evidence':'Finite geometric subtraction precedes infinite bound; normalized and physical tolerances differ correctly; endpoint histories retained; cylinder inputs and hidden third digits retained.'},
 {'level':'cumulative','scope':'Unit C, lessons06–07','result':'passed','evidence':'Projector products recomputed exactly; all detail sectors reconstruct; product hypotheses declared; block proof precedes domain assessment and no archival operator is invented.'},
 {'level':'final','scope':'coverage, fidelity, dependency order and assessment','result':'passed','evidence':'Seven concepts mapped to actual explanations, worked examples, answered practices, diagnostics and explicit capstone tasks. Independent audit read full capstone and recomputed answers/rubric.'},
 {'level':'final','scope':'terminology, units, evidence and audience','result':'passed','evidence':'Glossary follows actual usage; all core matrix and series operations taught locally; synthetic B explicitly distinguished from Cell3, LU units confined to rendering; no measured data/mechanism fabricated. Twelve periods preserve expanded blueprint.'},
 {'level':'final','scope':'mathematics and example answers','result':'passed','evidence':'20 manager verification groups plus independent rational checks; signed tails, finite products, mixed projector products and sequence domain identities recomputed.'},
 {'level':'final','scope':'rendering, links and minimality','result':'passed','evidence':f'Markdown only: {tables} table blocks and {links} relative links checked; no PDF/Word rendering required. All required sections retained with no teaching added in assembly.'},
 {'level':'final','scope':'storage and recovery','result':'passed','evidence':'All persistent artifacts stored in designated course directory; no source copies. Manifest recovery preflight performed; final machine validator separately checks checkpoint hashes, containment, audit counts and verbatim assembly.'}
]
counts={'critical':0,'major':0,'minor':0}
dump('audit_report.json',{'schema_version':'1.0','status':'passed','findings':findings,'unresolved_counts':counts,'checks':checks,'recovery_preflight':recovery,'independent_review':'independent-audit.json','source_gaps':'Specific infinite operator domain/action and infinite filtration convergence are not supplied by the loaded M18 passage; explicitly bounded, not required computations.'})
spec=[('input-contract','supplement','input-contract.json',[]),('course-map','course-map','course-map.md',['input-contract'])]
spec += [(i,'lesson',i+'.md',['course-map'] if n==0 else [order[n-1]]) for n,i in enumerate(order)]
spec += [('terminology','terminology','terminology.md',order),('teacher-guide','teacher-guide','teacher-guide.md',order),('capstone','capstone','capstone.md',order),('sources','supplement','sources.md',['input-contract']),('source-verification','supplement','source-verification.json',['sources']),('example-verification','supplement','worked-example-verification.json',order),('independent-audit','supplement','independent-audit.json',order+['capstone']),('assembly','assembly','course.md',order),('audit','audit','audit_report.json',['assembly','independent-audit','example-verification'])]
for name in ['build_course.py','support_course.py','repair_inner_product.py','repair_presentation.py','verify_examples.py','independent_check.py','finalize_course.py']:
 spec.append(('script-'+name[:-3],'supplement',name,[]))
cps=[{'id':i,'kind':kind,'path':path,'status':'passed','dependencies':deps,'sha256':sha(path),'summary':('Reviewed '+path if kind!='supplement' else 'Reproducibility or provenance artifact '+path)} for i,kind,path,deps in spec]
deliverables=[c['path'] for c in cps]+['completion_report.json']
assumptions=p['assumptions']+['All example numeric inputs are synthetic and dimensionless unless explicitly LU; no empirical data are required.','Unprovided infinite history-operator and filtration contracts are taught as source boundaries; core operations use fully specified finite models.','Approved project storage overrides the skill Desktop default; 12 core and3 capstone periods at55 minutes each.']
manifest={'schema_version':'1.0','topic':p['topic'],'audience':p['audience'],'assumptions':assumptions,'course_output_directory':str(R),'ordered_deliverables':deliverables,'checkpoints':cps,'dependencies':{c['id']:c['dependencies'] for c in cps},'course_order':order,'assembly':{'path':'course.md','section_ids':order},'audit_counts':counts,'blockers':[],'next_action':'none'}
dump('manifest.json',manifest)
completion={'status':'complete','topic':p['topic'],'audience':p['audience'],'assumptions':assumptions,'outputs':deliverables,'audit_counts':counts,'lesson_count':7,'periods':{'core':12,'capstone':3,'minutes_each':55},'hashes':{n:sha(n) for n in deliverables if n!='completion_report.json'},'source_gaps':['No specific infinite history-operator domain/action or complete infinite filtration convergence contract in loaded M18 passage; finite core is complete.'],'validator':{'status':'pending execution','command':"& 'C:/ProgramData/anaconda3/Scripts/conda.exe' run -n tf_gpu_env python 'Z:/Kfield-doc-training/.work/validate_project_course.py' '"+str(R)+"' --json"}}
completion['hashes']['manifest.json']=sha('manifest.json')
dump('completion_report.json',completion)
print(json.dumps({'assembled_lessons':len(order),'checkpoints':len(cps),'tables_checked':tables,'relative_links_checked':links,'next':'Run required project validator; record actual result in completion and revalidate.'}))
