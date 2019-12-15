import sys
import collections
import pprint

tree = collections.defaultdict(list)
orbits = sys.stdin.readlines()

direct = len(orbits)
for orbit in orbits:
    x,y = orbit.strip().split(')') 
    tree[x].append(y)
    tree[y].append(x)

def distance(tree, prev, curr, dest):
    children = tree[curr]
    d = 0
    if dest in children: 
        d = 1
    else: 
        d = sum([distance(tree, curr, node, dest) for node in children if node != prev])
        d += d > 0
    return d

total = -2
for key in tree.keys(): 
    d = distance(tree, key, key, 'COM')
    total += d
    
indirect = total - direct
print("direct", direct, "indirect", indirect, "total", total)
print("transfers", distance(tree, 'YOU', 'YOU', 'SAN') - 2)
