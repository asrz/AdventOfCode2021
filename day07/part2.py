def get_total_fuel(crabs, x):
    global fuels
    
    if x in fuels:
        return fuels[x]
    
    total = 0
    for crab in crabs:
        n = abs(crab - x)
        total += (n*(n+1))/2
    fuels[x] = total
    return total

fuels = {}

with open('input.in', 'r') as input_file:
    crabs = [int(x) for x in input_file.readline().split(',')]
    
    lo = 0
    hi = max(crabs)
    
    while abs(hi-lo) > 1:
        print(lo, hi)
        x = (hi - lo)/2 + lo
        
        if get_total_fuel(crabs, lo) < get_total_fuel(crabs, hi):
            hi = x
        else:
            lo = x
    
    print(min(get_total_fuel(crabs, hi), get_total_fuel(crabs, lo)))
