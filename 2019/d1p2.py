def get_fuel(mass): 
    fuel = int(mass)//3 - 2
    return 0 if (fuel < 0) else (fuel + get_fuel(fuel))

print reduce(
        lambda fuel, mass: get_fuel(mass) + fuel, 
        open('day1-input'), 
        0)
