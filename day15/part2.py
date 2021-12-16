import sys

import time

def get_next_node(visited, tentative_distance, potential_nodes):
    global height, width
    
    pair = None
    distance = sys.maxint
    
    for (x,y) in potential_nodes:
        if visited[y][x]:
            continue
        heuristic = (height + width) * 3
        dst = tentative_distance[y][x] + heuristic
        if dst < distance:
            pair = (x,y)
            distance = dst
                
    return pair

start = time.time()

with open('input.in', 'r') as input_file:
    grid = [map(int, list(line[:-1])) for line in input_file.readlines()]
    
    height = len(grid)
    width = len(grid[0])
    
    new_grid = [[0 for _ in range(width*5)] for _ in range(height*5)]
    
    for i in range(5):
        for j in range(5):
            for x in range(width):
                for y in range(height):
                    value = (grid[y][x] + i + j) % 9
                    if value == 0:
                        value = 9
                    new_grid[i*height + y][j*width + x] = value
            
    height *= 5
    width *= 5
    grid = new_grid
    
    visited = [[False for _ in range(width)] for _ in range(height)]
    
    tentative_distance = [[sys.maxint for _ in range(width)] for _ in range(height)]
    tentative_distance[0][0] = 0
    
    potential_nodes = set()
    potential_nodes.add((0,0))
    
    
    while not visited[height-1][width-1]:
        (x,y) = get_next_node(visited, tentative_distance, potential_nodes)
        
        for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            x2 = x + dx
            y2 = y + dy
        
            if x2 >= 0 and x2 < width and y2 >= 0 and y2 < height:
                if not visited[y2][x2]:
                    tentative_distance[y2][x2] = min(tentative_distance[y2][x2], tentative_distance[y][x] + grid[y2][x2])
                    potential_nodes.add((x2,y2))
        visited[y][x] = True
        potential_nodes.remove((x,y))
        
    print(tentative_distance[height-1][width-1])
    
print(time.time() - start, 'ms')