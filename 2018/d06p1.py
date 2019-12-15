import sys
import collections

coords = [tuple(map(int, l.split(", "))) for l in sys.stdin]
xs, ys = zip(*coords)

def distance(p1, p2): 
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

point_areas = collections.defaultdict(int)

bbx = min(xs)-1, max(xs)+1
bby = min(ys)-1, max(ys)+1
for x in range(bbx[0], bbx[1]+1):
    for y in range(bby[0], bby[1]+1):
        dists = [distance(p, (x,y)) for p in coords]
        min_points = [coord for dist, coord in zip(dists, coords) if dist == min(dists)]
        if len(min_points) == 1: 
            p = min_points[0]
            point_areas[p] += 1
            if x in bbx or y in bby: 
                point_areas[p] = -float('inf')

print(max(point_areas.values()))
