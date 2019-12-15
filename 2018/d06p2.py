import sys
import collections

coords = [tuple(map(int, l.split(", "))) for l in sys.stdin]
xs, ys = zip(*coords)

def distance(p1, p2): 
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


threshold = 10000
area = 0

bbx = min(xs), max(xs)
bby = min(ys), max(ys)
for x in range(bbx[0], bbx[1]+1):
    for y in range(bby[0], bby[1]+1):
        area += sum([distance(p,(x,y)) for p in coords]) < threshold

print(area)
