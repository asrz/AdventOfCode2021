def product(iterable):
    result = 1
    for num in iterable:
        result *= num
        
    return result

def check_neighbours(grid, basin, x, y):
    new_basin = set(list(basin)[:])
    
    #print('checking', x,y)
    
    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
        (x2,y2) = (x+dx, y+dy)
            
        if (x2,y2) not in basin:
            if x2 >= 0 and x2 < len(grid[y]) and y2 >= 0 and y2 < len(grid):
                num = grid[y2][x2]
                if num != 9 and num > grid[y][x]:
                    new_basin.add((x2,y2))
                    new_basin = new_basin.union(check_neighbours(grid, basin, x2, y2))
                    
    return new_basin
         

with open('input.in', 'r') as input_file:
    grid = [map(int, list(line[:-1])) for line in input_file.readlines()]
    
    basins = []
    
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
                
            basin = set()
            basin.add((x,y))
                
            basins.append(check_neighbours(grid, basin, x, y))
            
    #print(basins)    
    basin_sizes = map(len, basins)
    basin_sizes.sort(reverse=True)
    
    print(product(basin_sizes[:3]))
    
    
            
            