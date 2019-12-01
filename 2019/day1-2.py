import math

def get_fuel(mass): 
    fuel = math.floor(mass/3.0) - 2
    return 0 if (fuel < 0) else (fuel + get_fuel(fuel))

print reduce(
        lambda fuel, mass: get_fuel(mass) + fuel, 
        map(int, open('day1-input')), 
        0)
