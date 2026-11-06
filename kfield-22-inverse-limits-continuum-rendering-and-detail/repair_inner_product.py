from pathlib import Path
R=Path(__file__).resolve().parent
old='The finite dot-product inequality bounds partial inner products by the product of the two norms, so these inner products converge for ℓ² sequences.'
new='''To justify this infinite inner product, first prove a finite inequality. For lists a₁,…,a_N and b₁,…,b_N, put A=Σa_n², B=Σb_n² and C=Σa_n b_n, where these three sums stop at N. If B=0, every b_n is zero and C=0. If B>0, the sum of squares Σ(a_n−t b_n)²=A−2tC+t²B is nonnegative for every real t. Choose t=C/B to obtain A−C²/B≥0, hence |C|≤√A√B. This is the finite dot-product inequality. Apply it to a_n=|x_n| and b_n=|y_n|: each finite sum Σ|x_n y_n| is at most ||x||₂||y||₂. These nonnegative partial sums increase and stay bounded, so they converge. Thus the signed inner product converges absolutely: the total size of every remaining signed tail is bounded by the corresponding absolute tail, which tends to zero. Merely bounded signed partial sums would not be enough. The temporary finite-sum names A,B,C in this proof are scalars; B here is not the length-valued matrix of Lesson04.'''
for name in ['lesson-07.md','build_course.py']:
    path=R/name
    text=path.read_text(encoding='utf-8')
    assert old in text
    path.write_text(text.replace(old,new),encoding='utf-8')
print('Inner product proof repaired in lesson and authored source.')
