'''
Created on Dec. 3, 2021

@author: Alex
'''

with open('input.in', 'r') as input_file:
    
    aim = 0
    horizontal = 0
    depth = 0
    
    for line in input_file:
        (direction, x) = line.split()
        if direction == 'forward':
            horizontal += int(x)
            depth += aim * int(x)
        elif direction == 'up':
            aim -= int(x)
        elif direction == 'down':
            aim += int(x)
        else:
            print('wtf')
            exit()
            
    print horizontal, depth, horizontal * depth