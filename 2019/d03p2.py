import sys
import collections

def distance(p, steps): 
    return sum(steps[p].values())

grid = collections.defaultdict(set)
steps = collections.defaultdict(dict)
wire = 0

for line in sys.stdin:
    x, y = (0,0)
    step = 0
    for mov in line.strip().split(","):
        direct = mov[0]
        dist = int(mov[1:])
        for delta in range(dist):
            if direct == "U":
                    y += 1 
            elif direct == "D":
                    y -= 1 
            elif direct == "L":
                    x -= 1 
            elif direct == "R":
                    x += 1 
            step += 1
            grid[(x,y)].add(wire)
            if wire not in steps[(x,y)]:
                steps[(x,y)][wire] = step
    wire += 1

print(min([distance(p,steps) for p,w in grid.items() if len(w) > 1]))
