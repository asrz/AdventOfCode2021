with open('input.in', 'r') as input_file:
    grid = [map(int, list(line[:-1])) for line in input_file.readlines()]
    
    low_points = []
    
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            cell = grid[y][x]
            
            if y > 0:
                if grid[y-1][x] <= cell:
                    continue
                
            if y < len(grid)-1:
                if grid[y+1][x] <= cell:
                    continue
            
            if x > 0:
                if grid[y][x-1] <= cell:
                    continue
                
            if x < len(grid[y])-1:
                if grid[y][x+1] <= cell:
                    continue
                
            low_points.append(cell)
            
    print sum(low_points) + len(low_points)
            
            