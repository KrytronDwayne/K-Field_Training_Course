"""Record C24-IND-001 repair without regenerating passed student material."""
from pathlib import Path
import ast, hashlib, json

root = Path(__file__).parent
def read(name):
    return json.loads((root / name).read_text(encoding='utf-8'))
def digest(name):
    return hashlib.sha256((root / name).read_bytes()).hexdigest()
def save(name, value):
    (root / name).write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

manifest = read('manifest.json')
completion = read('completion_report.json')
for checkpoint in manifest['checkpoints']:
    assert digest(checkpoint['path']) == checkpoint['sha256'], checkpoint['id']
for name, expected in completion['hashes'].items():
    assert digest(name) == expected, name
tree = ast.parse((root/'author_course.py').read_text(encoding='utf-8'))
checked = []
for node in tree.body:
    if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id == 'lesson':
        call = node.value
        number = ast.literal_eval(call.args[0])
        body = ast.literal_eval(call.args[2]).strip()
        name = f'lesson-{number:02}.md'
        assert body in (root/name).read_text(encoding='utf-8'), name
        checked.append(name)
assert len(checked) == 7
sentence = 'Both R and o remain constant throughout the velocity interval for this example.'
assert sentence in (root/'author_course.py').read_text(encoding='utf-8')
audit = read('audit_report.json')
record = dict(id='C24-IND-001', level='final', category='authoring_recovery_regression', severity='minor', file='author_course.py', section='lesson(1), C24.01-W1 authored body', defect='Authoring body retained the old origin-only sentence and would remove the existing fixed-R/fixed-o clarification on regeneration.', correction='Propagated the exact repaired sentence from current lesson-01.md into the authoring literal; no student or mathematical content changed.', verification='AST extraction confirmed all seven literal authored bodies match their current lesson text. Existing checkpoint and completion hashes verified before updating recovery records. Independent auditor report remains unchanged; external recheck pending.', disposition='corrected', affected_checkpoints=['lesson-01','assembly','audit','authoring-recovery'])
audit['findings'] = [f for f in audit['findings'] if f['id'] != record['id']] + [record]
save('audit_report.json', audit)
checkpoint = dict(id='authoring-recovery', kind='supplement', path='author_course.py', dependencies=[], status='passed', sha256=digest('author_course.py'), summary='Retained authoring literals match all seven current lesson bodies; C24-IND-001 fixed.')
manifest['checkpoints'] = [c for c in manifest['checkpoints'] if c['id'] != checkpoint['id']] + [checkpoint]
for item in manifest['checkpoints']:
    item['sha256'] = digest(item['path'])
manifest['dependencies'] = {c['id']: c['dependencies'] for c in manifest['checkpoints']}
if 'author_course.py' not in manifest['ordered_deliverables']:
    manifest['ordered_deliverables'].insert(-1, 'author_course.py')
save('manifest.json', manifest)
completion['outputs'] = manifest['ordered_deliverables']
completion['hashes'] = {name:digest(name) for name in completion['outputs'] if name != 'completion_report.json'} | {'manifest.json':digest('manifest.json')}
completion['follow_up_repair'] = {'finding':'C24-IND-001','status':'corrected; independent recheck pending','verification':'Seven AST-extracted lesson bodies match current teaching text; retained authoring script now hash-tracked.'}
save('completion_report.json', completion)
print('Seven authored bodies match; passed content hashes verified; audit and recovery hashes refreshed.')
