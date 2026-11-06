from pathlib import Path
R=Path(__file__).resolve().parent
changes={
 'terminology.md':[('|ℓ², ||x||₂|','|ℓ², sequence 2-norm|')],
 'sources.md':[('/backbone_sequence/17/proof/0–2','/backbone_sequence/17/proof/0, /backbone_sequence/17/proof/1, /backbone_sequence/17/proof/2'),('/backbone_sequence/3/proof/0–4','/backbone_sequence/3/proof/0, /backbone_sequence/3/proof/1, /backbone_sequence/3/proof/2, /backbone_sequence/3/proof/3, /backbone_sequence/3/proof/4')],
 'lesson-04.md':[('/proof/1–2','/backbone_sequence/17/proof/1 and /backbone_sequence/17/proof/2')]
}
for name,repls in changes.items():
    f=R/name;s=f.read_text(encoding='utf-8')
    for a,b in repls:
        assert a in s,(name,a)
        s=s.replace(a,b)
    f.write_text(s,encoding='utf-8')
# Keep authored build scripts aligned without regenerating reviewed content.
for name in ['support_course.py','build_course.py']:
    f=R/name;s=f.read_text(encoding='utf-8')
    for repls in changes.values():
        for a,b in repls:s=s.replace(a,b)
    f.write_text(s,encoding='utf-8')
print('Table cell and exact source locators corrected.')
