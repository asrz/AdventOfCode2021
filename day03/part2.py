'''
Created on Dec. 3, 2021

@author: Alex
'''

with open('input.in', 'r') as input_file:
    lines = [line[:-1] for line in input_file.readlines()]
    
    oxygen = ''
    co2 = ''
    
    o_candidates = lines
    
    for i in range(len(lines[0])):
        counts = [0, 0]
        for j in range(len(o_candidates)):
            counts[int(o_candidates[j][i])] += 1
            
        if counts[0] > counts[1]:
            o_candidates = [candidate for candidate in o_candidates if candidate[i] == '0']
        else:
            o_candidates = [candidate for candidate in o_candidates if candidate[i] == '1']
            
        if len(o_candidates) == 1:
            oxygen = o_candidates[0]
    
    c_candidates = lines

    for i in range(len(lines[0])):
        counts = [0, 0]
        for j in range(len(c_candidates)):
            counts[int(c_candidates[j][i])] += 1
            
        if counts[0] > counts[1]:
            c_candidates = [candidate for candidate in c_candidates if candidate[i] == '1']
        else:
            c_candidates = [candidate for candidate in c_candidates if candidate[i] == '0']
            
        if len(c_candidates) == 1:
            co2 = c_candidates[0]

    
    print oxygen, co2, int(oxygen, 2) * int(co2, 2)
            