from itertools import combinations
"""
ins = input().split()
if len(ins) == 1:
    per = permutations(ins[0], len(ins[0]))
else:
    per = permutations(ins[0], int(ins[1]))

for i in sorted(per):
    res = ''
    for j in range(len(i)):
        res = res+i[j]
    print(res.upper())"""
from itertools import combinations, chain

S, k = input().split()
S, k = sorted(S), int(k)

for each in chain.from_iterable([combinations(S, i) for i in range(1, k+1)]):
    print(''.join(each))