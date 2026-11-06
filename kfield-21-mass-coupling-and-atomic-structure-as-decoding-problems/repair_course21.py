from pathlib import Path
import json
from fractions import Fraction as F
R=Path(__file__).parent
def edit(name,old,new):
    p=R/name;s=p.read_text(encoding='utf-8');assert s.count(old)==1,(name,old,s.count(old));p.write_text(s.replace(old,new),encoding='utf-8')
old='Keep a_e symbolic when absent; keep m/m_e symbolic when m_e is absent. No numerical physical mass is requested from missing inputs.'
new='If a contributing renderer entry is missing, keep its term symbolic; for example, an absent a_e leaves c5 a_e symbolic when c5 is nonzero. If only the numerical reference mass m_e is absent, compute the dimensionless ratio m/m_e=c dot b from the supplied entries and retain m=(c dot b)m_e symbolically. Only the numerical dimensional mass remains unresolved in that case.'
for name in ['build_course.py','lesson-04.md']:edit(name,old,new)
old_boundary='Neither b nor a solver chooses a physical occupied c. If a_e or m_e is absent, return the symbolic renderer and missing input status. A rounded report 2.33 is not exact 7/3; retain their difference.'
new_boundary='Neither b nor a solver chooses a physical occupied c. Missing contributing renderer entries leave their terms symbolic. If only m_e is absent, report the computable dimensionless ratio c dot b and retain m=(c dot b)m_e symbolically; the numerical dimensional mass is unresolved. A rounded report 2.33 is not exact 7/3; retain their difference.'
edit('lesson-04.md',old_boundary,new_boundary)
edit('build_course.py',"txt+='**Boundary to carry forward:** '+a['diagnostic']['task_and_answer']+'\\n\\n'", "boundary="+repr(new_boundary)+" if n==4 else a['diagnostic']['task_and_answer']\n    txt+='**Boundary to carry forward:** '+boundary+'\\n\\n'")
practice='''### Answered practice: reference mass withheld

Use the existing synthetic c=(1,0,0,0,0,1) and b_toy=(1,1/10,1/100,1/1000,1/5,2), but withhold the numerical value of m_ref. Find the ratio and state exactly what remains unresolved.

**Answer:** c dot b_toy=1+2=3, so m/m_ref=3 and m=3*m_ref. The dimensionless ratio is completely computed. The numerical dimensional mass remains unresolved until m_ref is supplied. Keep the coefficient and syndrome records; withholding the reference mass does not erase their known values.

'''
edit('lesson-04.md','<a id="C21.04-D1"></a>',practice+'<a id="C21.04-D1"></a>')
edit('build_course.py',"    txt+=anchor(a['diagnostic']['id'])",'    if n==4: txt+='+repr(practice)+'\n    txt+=anchor(a[\'diagnostic\'][\'id\'])')
edit('terminology.md','| R / Z | Real-number field / integers. Bold or contextual R for reals is separate from projector R. | 02 |','| R / Z | Real-number field / integers. Bold or contextual R for reals is separate from projector R. | R: 01; Z: 02 |')
edit('terminology.md','| b / b_toy | Source renderer order (1,alpha,alpha²,alpha³,a_e,eta) / separately stipulated toy values. | 04 |','| b / b_toy | Source renderer order (1,alpha,alpha²,alpha³,a_e,eta) / separately stipulated toy values. | b: 03 (rendering 04); b_toy: 04 |')
edit('build_course.py',"('R / Z','Real-number field / integers. Bold or contextual R for reals is separate from projector R.','02')","('R / Z','Real-number field / integers. Bold or contextual R for reals is separate from projector R.','R: 01; Z: 02')")
edit('build_course.py',"('b / b_toy','Source renderer order (1,alpha,alpha²,alpha³,a_e,eta) / separately stipulated toy values.','04')","('b / b_toy','Source renderer order (1,alpha,alpha²,alpha³,a_e,eta) / separately stipulated toy values.','b: 03 (rendering 04); b_toy: 04')")
p=R/'course.md';s=p.read_text();begin='<!-- BEGIN: lesson-04 -->\n';end='\n<!-- END: lesson-04 -->';i=s.index(begin)+len(begin);j=s.index(end,i);p.write_text(s[:i]+(R/'lesson-04.md').read_text().rstrip('\n')+s[j:],encoding='utf-8')
c=[1,0,0,0,0,1];b=list(map(F,['1','1/10','1/100','1/1000','1/5','2']));ratio=sum(x*y for x,y in zip(c,b));assert ratio==3
compile((R/'build_course.py').read_text(),'build_course.py','exec')
print('Targeted repairs applied; exact withheld-reference ratio =',ratio)
