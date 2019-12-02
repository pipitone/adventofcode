import sys
import itertools
idents = sys.stdin.read().strip().split()
for i, j in itertools.product(idents,idents):
    distance = sum([c1 != c2 for c1, c2 in zip(i,j)])
    if distance == 1: 
        print(''.join([ c1 for c1, c2 in zip(i,j) if c1 == c2]))
        break
# lsrivmotzbdxpkxnaqmuwcchj
