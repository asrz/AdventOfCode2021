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


def get_score(char):
    if char == '(':
        return 1
    elif char == '[':
        return 2
    elif char == '{':
        return 3
    elif char == '<':
        return 4
    else:
        print('wtf', char)
        exit()

def get_incompleteness_score(line):
    stack = []
    for char in list(line):
        if char in ('(', '[', '{', '<'):
            stack.append(char)
        elif char in (')', ']', '}', '>'):
            char0 = stack.pop()
            if not is_pair(char, char0):
                return 0
    
    score = 0
    for char in reversed(stack):
        score *= 5
        score += get_score(char)
        
    return score
        

with open('input.in', 'r') as input_file:
    scores = map(get_incompleteness_score, input_file.readlines())
    
    scores = filter(lambda score : score > 0, scores)
    
    scores.sort()
    
    print scores[len(scores)//2]
        
        
        
                    
                
                