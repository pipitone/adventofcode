import sys
import functools

def get_fuel(mass): 
    fuel = int(mass)//3 - 2
    return 0 if (fuel < 0) else (fuel + get_fuel(fuel))

fuel = reduce(lambda fuel, mass: get_fuel(mass) + fuel, sys.stdin, 0)
print(fuel)
