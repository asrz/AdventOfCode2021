import re


with open('input.in', 'r') as input_file:
    lines = []
    
    pattern = r'(\d+),(\d+) -> (\d+),(\d+)'
    
    max_val = 0
    
    for line in input_file.readlines():
        (x1, y1, x2, y2) = [int(x) for x in re.match(pattern, line[:-1]).groups()]
        
        max_val = max(max_val, x1, y1, x2, y2)
        
        lines.append((x1, y1, x2, y2))
        
    max_val += 1
    board = [[0 for _ in range(max_val)] for _ in range(max_val)]
    
    #print(lines)
    
    for line in lines:
        (x1, y1, x2, y2) = line
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                board[y][x1] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                board[y1][x] += 1
        elif (x1-x2) * (y1-y2) > 0:
            for i in range(abs(x1-x2)+1):
                board[min(y1,y2)+i][min(x1,x2)+i] += 1
        else:
            for i in range(abs(x1-x2)+1):
                board[min(y1,y2)+i][max(x1,x2)-i] += 1
        #print(line)
        #for row in board:
        #    print(row)
    count = 0
    for row in board:
        for cell in row:
            if cell > 1:
                count += 1
    print(count)
    
    #for row in board:
    #    print(row)