'''
Created on Dec. 3, 2021

@author: Alex
'''

with open('input.in', 'r') as input_file:
    lines = [line[:-1] for line in input_file.readlines()]
    
    gamma = ''
    epsilon = ''
    
    for i in range(len(lines[0])):
        counts = [0, 0]
        for j in range(len(lines)):
            counts[int(lines[j][i])] += 1
            
        if counts[0] > counts[1]:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
            
    print int(gamma, 2) * int(epsilon, 2)
            