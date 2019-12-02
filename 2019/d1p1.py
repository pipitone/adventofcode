def get_fuel(mass): 
    fuel = int(mass)//3.0 - 2
    return fuel

print reduce(
        lambda fuel, mass: get_fuel(mass) + fuel, 
        open('day1-input'), 
        0)
