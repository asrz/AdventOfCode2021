import re

with open('input.in', 'r') as input_file:
    points = []
    folds = []
    
    for line in input_file.readlines():
        if ',' in line:
            (x, y) = [int(i) for i in line[:-1].split(',')]
            points.append((x,y))
        if line.startswith('fold'):
            folds.append(re.match(r'fold along (y|x)=(\d+)', line).groups())
            
    height = 0
    width = 0
    for (x,y) in points:
        height = max(height, y)
        width = max(width,x)
    
    height += 1
    width += 1
    
    grid = [list('.'*width) for _ in range(height)]
    
    for (x,y) in points:
        grid[y][x] = '#'
    
    
    for fold in folds:
        k = int(fold[1])
    
        if fold[0] == 'y':
            new_grid = [list('.'*width) for _ in range(k)]
            
            for y in range(len(grid)):
                for x in range(len(grid[y])):
                    if grid[y][x] == '#':
                        if y < k+1:
                            new_grid[y][x] = '#'
                        else:
                            new_grid[2*k - y][x] = '#'
            
        else:
            new_grid = [list('.'*k) for _ in range(height)]
            
            for y in range(len(grid)):
                for x in range(len(grid[y])):
                    if grid[y][x] == '#':
                        if x < k+1:
                            new_grid[y][x] = '#'
                        else:
                            new_grid[y][2*k - x] = '#'
        
        grid = new_grid
    
    for row in grid:
        print ''.join(map(str, row))

    