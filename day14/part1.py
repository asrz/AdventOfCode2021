with open('input.in', 'r') as input_file:
    polymer = input_file.readline()[:-1]
    
    input_file.readline()
    
    rules = {}
    line = input_file.readline()[:-1]
    
    while line != '':
        (a,b) = line.split(' -> ')
        rules[a] = b
        line = input_file.readline()[:-1]
    
    
    next_step = ''
    for j in range(10):
        for i in range(len(polymer)-1):
            pair = polymer[i:i+2]
            next_step += pair[0]
            next_step += rules[pair]
        next_step += polymer[-1]
    
        polymer = next_step
        next_step = ''
        
    counts = {}
    for char in set(polymer):
        counts[char] = polymer.count(char)
        
    print(max(counts.values()) - min(counts.values()))
    
    