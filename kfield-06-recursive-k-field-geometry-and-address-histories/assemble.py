from pathlib import Path
p=Path(__file__).parent
s=p/'sources.md';s.write_text(s.read_text(encoding='utf-8').replace('and /boundary_rule','and S02 /backbone_sequence/1/boundary_rule').replace('and /recursions','and S02 /backbone_sequence/2/recursions'),encoding='utf-8')
text='# Recursive K-Field Geometry and Address Histories\n\nSix lessons, seven core periods, two capstone periods.\n\nUse [course map](course-map.md), [terminology](terminology.md), [teacher guide](teacher-guide.md), [capstone with answers](capstone.md), and [sources](sources.md).\n\n'
for i in range(1,7):
 key=f'lesson-{i:02d}'
 text+=f'<!-- BEGIN: {key} -->\n'+(p/(key+'.md')).read_text(encoding='utf-8-sig').rstrip('\n')+f'\n<!-- END: {key} -->\n\n'
(p/'course.md').write_text(text,encoding='utf-8')
