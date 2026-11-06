from pathlib import Path
import json
p=Path(r'Z:/Kfield-doc-training/K-Field_Training_Course/kfield-06-recursive-k-field-geometry-and-address-histories')
c=json.loads((p/'input-contract.json').read_text(encoding='utf-8-sig'))
x=json.loads(Path(c['sources'][2]['path']).read_text(encoding='utf-8'))
for k in ['authority_contract','findings']: print(k,json.dumps(x[k],indent=2))
