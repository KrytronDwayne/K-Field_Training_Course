# Source comparison ledger

G01#/observed_27_node_occupancy. All seven sheets are retained; these are stored source fractions, not raw catalog copies. Decimal subtraction is performed on stored lexemes. Source identity and exact path are in sources.md.

| Sheet | Discovery | Holdout | Rotation mean | Holdout − discovery | Holdout − rotation mean |
|---|---|---|---|---|---|
| -3 | 0.012264349288667742 | 0.012634150597679085 | 0.013645318907599673 | 0.000369801309011343 | -0.001011168309920588 |
| -2 | 0.08975751629406406 | 0.09034115696710583 | 0.09301731960561899 | 0.00058364067304177 | -0.00267616263851316 |
| -1 | 0.23009671315439065 | 0.23092225809266206 | 0.23276214989965968 | 0.00082554493827141 | -0.00183989180699762 |
| 0 | 0.32384890321676363 | 0.3213855684495245 | 0.31476847570020083 | -0.00246333476723913 | 0.00661709274932367 |
| 1 | 0.24011843857313056 | 0.24245702818253206 | 0.23893643661111605 | 0.00233858960940150 | 0.00352059157141601 |
| 2 | 0.0910890742168337 | 0.08957333566006456 | 0.09335079835965442 | -0.00151573855676914 | -0.00377746269958986 |
| 3 | 0.012825005256149696 | 0.012686502050431899 | 0.013519500916150435 | -0.000138503205717797 | -0.000832998865718536 |

Stored-fraction sum remainders from one:
- discovery: 3.8E-17
- holdout: -6E-18
- rotation mean: 7.8E-17

All 27 available state labels, grouped by sheet (these are combinatorial labels, not observed counts):

- -3: (-1, -1, -1)
- -2: (-1, -1, 0), (-1, 0, -1), (0, -1, -1)
- -1: (-1, -1, 1), (-1, 0, 0), (-1, 1, -1), (0, -1, 0), (0, 0, -1), (1, -1, -1)
- 0: (-1, 0, 1), (-1, 1, 0), (0, -1, 1), (0, 0, 0), (0, 1, -1), (1, -1, 0), (1, 0, -1)
- 1: (-1, 1, 1), (0, 0, 1), (0, 1, 0), (1, -1, 1), (1, 0, 0), (1, 1, -1)
- 2: (0, 1, 1), (1, 0, 1), (1, 1, 0)
- 3: (1, 1, 1)

The full empirical 27-state vectors are not supplied in this small G01 summary. The course retains their source reference and does not fabricate their entries or claim to replay the reported correlation. G02 pp17–19 reports the full-state analysis. The source pure-coordinate family result remains separate from the mixed branch-lift occupancy.
