def add_count(dict, key, count):
    if key not in dict:
        dict[key] = 0
    
    dict[key] += count
        

with open('input.in', 'r') as input_file:
    polymer = input_file.readline()[:-1]
    
    input_file.readline()
    
    rules = {}
    line = input_file.readline()[:-1]
    
    while line != '':
        (a,b) = line.split(' -> ')
        rules[a] = b
        line = input_file.readline()[:-1]
    
    
    pairs = {}
    for i in range(len(polymer)-1):
        add_count(pairs, polymer[i:i+2], 1)
    
    
    next_pairs = {}
    for j in range(40):
        for pair in pairs:
            count = pairs[pair]
            
            char = rules[pair]
            head = pair[0] + char
            tail = char + pair[1]
            
            add_count(next_pairs, head, count)
            add_count(next_pairs, tail, count)
    
        pairs = next_pairs
        next_pairs = {}
        
    counts = {}
    for pair in pairs:
        (head, tail) = list(pair)
        add_count(counts, head, pairs[pair])
        add_count(counts, tail, pairs[pair])
    
    #everything is double counted except first and last which never change
    counts[polymer[0]] += 1
    counts[polymer[-1]] += 1
    
    print((max(counts.values()) - min(counts.values()))/2)
    
    