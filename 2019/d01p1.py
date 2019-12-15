import sys
import functools 

def get_fuel(mass): 
    fuel = int(mass)//3.0 - 2
    return fuel

fuel = functools.reduce(lambda fuel, mass: get_fuel(mass) + fuel, sys.stdin, 0)
print(fuel)
