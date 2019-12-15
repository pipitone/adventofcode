import sys
import re
import collections
steps = map(lambda x: re.findall('[A-Z]', x[1:]), sys.stdin)
depends = collections.defaultdict(set)
for pre,post in steps:
    depends[pre].update([])
    depends[post].add(pre)

order = []
while len(depends) > 0: 
    avail = sorted([ k for k,v in depends.items() if not v ])
    step = avail.pop(0)
    order.append(step)
    del depends[step]
    for i in depends.keys(): 
        depends[i].discard(step)

print(''.join(order))
