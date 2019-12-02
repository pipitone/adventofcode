import sys
import re
import collections
import itertools

# i,ldx,tdx,w,h 
claims = map(lambda line: map(int, re.findall("\d+", line)), sys.stdin)
fabric = collections.defaultdict(list)
for i,ldx,tdx,w,h in claims:
    for x,y in itertools.product(xrange(ldx,ldx+w), xrange(tdx,tdx+h)):
        fabric[(x,y)].append(i)

overlapping_points = [v for k,v in fabric.iteritems() if len(v) > 1]
print(len(overlapping_points)) # 111485
overlapping_claims = set(itertools.chain(*overlapping_points))
print(set([i for i,_,_,_,_ in claims]) - overlapping_claims) # set([113])

