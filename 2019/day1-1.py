import math

def get_fuel(mass): 
    fuel = math.floor(mass/3.0) - 2
    return fuel

print reduce(
        lambda fuel, mass: get_fuel(mass) + fuel, 
        map(int, open('day1-input')), 
        0)
