import math

def explode(number, i):
    start = i-1
    left = ''
    right = ''
    char = number[i]
    while char != ',':
        left += char
        i+= 1
        char = number[i]
    i += 1 # skip comma
    char = number[i]
    while char != ']':
        right += char
        i += 1
        char = number[i]
    i += 1
    end = i
    
    left = int(left)
    right = int(right)
    
    head_indices = [0, 0]
    i = start - 1
    while i > 0 and not is_digit(number[i]):
        i -= 1
    if i > 0:
        head_indices[1] = i+1
        while is_digit(number[i]):
            i -= 1
        head_indices[0] = i+1
        
        head = number[head_indices[0]:head_indices[1]]
        new_head = str(int(head) + left)
        start += len(new_head) - len(head)
        end += len(new_head) - len(head)
        number = number[:head_indices[0]] + str(new_head) + number[head_indices[1]:]
    
    tail_indices = [0, 0]
    i = end + 1
    while i < len(number) and not is_digit(number[i]):
        i += 1
    if i < len(number):
        tail_indices[0] = i
        while is_digit(number[i]):
            i += 1
        tail_indices[1] = i
        
        tail = int(number[tail_indices[0]:tail_indices[1]]) + right
        number = number[:tail_indices[0]] + str(tail) + number[tail_indices[1]:]
    
#     print (number[:start], number[start:end], number[end:])
    number = number[:start] + '0' + number[end:]
    return number
    

def split(number, start, end):
    num = number[start:end]
    num = int(num)
    
    left = str(int(math.floor(num/2.0)))
    right = str(int(math.ceil(num/2.0)))
    
    return number[:start] + '[' + left + ',' + right + ']' + number[end:]

def is_digit(char):
    o = ord(char)
    return o >= 48 and o <= 57 #between 0 and 9

def reduce(number):
#     print('reducing', number)
    depth = 0
    
    i = 0
    while i < len(number):
        char = number[i]
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
        elif depth > 4:
            return reduce(explode(number, i))
            
        i += 1
    
    i = 0
    curr = ''
    while i < len(number):
        char = number[i]
        
        if is_digit(char):
            curr += char
        elif len(curr) > 1:
            return reduce(split(number, i - len(curr), i))
        else:
            curr = ''
        
        i += 1
    return number

def add(number1, number2):
    if number1 is None:
        return number2
    
    return reduce('[' + number1 + ',' + number2 + ']')

def magnitude(number):
    if ',' not in number:
        return int(number)
    
    left = ''
    right = ''
    
    i = 1
    depth = 0
    while i < len(number):
        char = number[i]
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
        elif char == ',' and depth == 0:
            left = number[1:i]
            right = number[i+1:-1]
        i += 1
        
        
    return 3 * magnitude(left) + 2 * magnitude(right)

with open('input.in', 'r') as input_file:
    number = None
    for line in [line[:-1] for line in input_file.readlines()]:
        number = add(number, line)

        
    print(magnitude(number))
