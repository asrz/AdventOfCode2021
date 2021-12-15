def is_pair(char, char0):
    if char == ')':
        return char0 == '('
    elif char == ']':
        return char0 == '['
    elif char == '}':
        return char0 == '{'
    elif char == '>':
        return char0 == '<'
    else:
        return False


def get_corruption_score(line):
    stack = []
    for char in list(line):
        if char in ('(', '[', '{', '<'):
            stack.append(char)
        elif char in (')', ']', '}', '>'):
            char0 = stack.pop()
            if not is_pair(char, char0):
                if char == ')':
                    return 3
                if char == ']':
                    return 57
                if char == '}':
                    return 1197
                if char == '>':
                    return 25137
    
    return 0
        

with open('input.in', 'r') as input_file:
    print(sum(map(get_corruption_score, input_file.readlines())))
        
        
                    
                
                