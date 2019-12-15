import sys
import re
import operator

data = map(lambda x: map(int, re.findall('-?\d+', x)), sys.stdin)
x,y,vx,vy = zip(*data)
points = list(zip(x,y))
bbox_x = (min(x), max(x)+1)
bbox_y = (min(y), max(y)+1)

for step in range(10647):
    bbox_x = (min(x), max(x)+1)
    bbox_y = (min(y), max(y)+1)

    print(step, (min(x) - max(x)) * (min(y) - max(y)))
    if step > 10644: 
        for j in range(bbox_y[0], bbox_y[1],  1):
            for i in range(*bbox_x):
                if (i,j) in points:
                    print('#', end='')
                else:
                    print('.', end ='')
            print(end='\n')
    x = list(map(operator.add, x, vx))
    y = list(map(operator.add, y, vy))
    points = list(zip(x,y))
