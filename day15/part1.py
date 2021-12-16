import sys

def get_next_node(visited, tentative_distance):
    pair = None
    distance = sys.maxint
    
    for y in range(len(visited)):
        for x in range(len(visited[y])):
            if visited[y][x]:
                continue
            dst = tentative_distance[y][x]
            if dst < distance:
                pair = (x,y)
                distance = dst
                
    return pair

with open('input.in', 'r') as input_file:
    grid = [map(int, list(line[:-1])) for line in input_file.readlines()]
    
    height = len(grid)
    width = len(grid[0])
    
    visited = [[False for _ in range(width)] for _ in range(height)]
    
#     for row in grid:
#         print ''.join(map(str, list(row)))
        
    tentative_distance = [[sys.maxint for _ in range(width)] for _ in range(height)]
    tentative_distance[0][0] = 0
    
    
    while not visited[height-1][width-1]:
        (x,y) = get_next_node(visited, tentative_distance)
        
        for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            x2 = x + dx
            y2 = y + dy
        
            if x2 >= 0 and x2 < width and y2 >= 0 and y2 < height:
                if not visited[y2][x2]:
                    tentative_distance[y2][x2] = min(tentative_distance[y2][x2], tentative_distance[y][x] + grid[y2][x2])
        visited[y][x] = True
        
    print(tentative_distance[height-1][width-1])