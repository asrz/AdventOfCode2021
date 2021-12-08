'''
Created on Dec. 1, 2021

@author: Alex
'''


with open('day1.in', 'r') as input_file:
    numbers = [int(x) for x in input_file.readlines()]
    
    count = 0
    for i in range(3, len(numbers)):
        if numbers[i] > numbers[i-3]:
            count += 1
            
    print(count)