from multiprocessing import Pool
import itertools
import sys 
serial = 7315
dim = 300

def power(x, y, serial):
    rack_id = x + 10
    p = rack_id * (y * rack_id + serial)
    p = p // 100 - p // 1000 * 10 - 5
    return p

def square_power(x,y, serial, size = 3): 
    # power of the square located at this loc
    return sum([ power(i,j, serial) for i in range(x,x+size) for j in range(y,y+size) ])

def make_grid(dim, serial, size):
    return { square_power(x,y,serial,size) : (x,y) for x in range(1, dim-size+2) for y in range(1, dim-size+2) }

def max_power(size):
    grid = make_grid(dim, serial, size)
    maxpower = max(grid.keys())
    return maxpower, (grid[maxpower], size) 

def get_squares(x,y,dim,serial):
    #if x % 5 == 0 or y % 5 == 0: 
    #    print(x,y)

    shells = []
    for l in range(0, min(dim-x, dim-y)):
        bottom = [power(x+i, y+l, serial) for i in range(0,l)]
        side = [power(x+l, y+i, serial) for i in range(0,l-1)]
        shells.append(sum(bottom) + sum(side))
    return (x,y), itertools.accumulate(shells)

if __name__ == "__main__": 
    #print("loc, power", max_power(size=3), "size", 3)
    #with Pool(4) as p:
    #    power_size = dict(p.map(max_power, range(1,dim+1)))
    #size_power = { size : max_power(dim, serial, size) for size in range(1,dim+1) }
    #power_size = { p : (loc, size) for size, (loc,p) in size_power.items() }
    #maxpower = max(power_size.keys())
    #print("loc, size", power_size[maxpower], "power", maxpower)

    # build up squares from 1 to as large as possible at that coordinate
    # We do this by first computing the bottom and right most edge sums
    # for increasing dimensions

    # power : (loc, size)
    serial = 18
    dim = 300 
    power_map = {}
    def curried_get_squares(coords): 
        x, y = coords
        return get_squares(x, y, dim, serial)

    with Pool(int(sys.argv[1])) as p: 
        squares = dict(p.map(curried_get_squares, 
            [(x,y) for x in range(1, dim+1) for y in range(1,dim+1)]))

    #for x in range(1, dim+1): 
    #    for y in range(1, dim+1):
    #        squares = get_squares(x,y,dim,serial)
    #        for l, p in squares:
    #            power_map[p] = (x,y,l)

    for coords, squarelist in squares.items():
        for l,p in enumerate(squarelist):
            power_map[p] = coords, l

    mpower = max(power_map.keys())
    print(mpower, power_map[mpower])
