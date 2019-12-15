import sys
import collections

def distance(p1, p2): 
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

grid = collections.defaultdict(set)
wire = 0

for line in sys.stdin:
    x, y = (0,0)
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
            grid[(x,y)].add(wire)
    wire += 1

print(min([distance((0,0),p) for p,w in grid.items() if len(w) > 1]))
