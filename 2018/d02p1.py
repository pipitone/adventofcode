import sys
import collections
twice = 0 
thrice = 0

for ident in sys.stdin: 
    c = collections.Counter(ident)
    twice += 2 in c.values()
    thrice += 3 in c.values()

print(twice * thrice)
# 7688
