def is_small(cave):
    return cave == cave.lower()

def dfs(paths, path, routes):
    curr = path[-1]
    
    if curr == 'end':
        routes.append(path)
    
    options = paths[curr]
    
    for option in options:
        if is_small(option) and option in path:
            continue
        new_path = path[:]
        new_path.append(option)
        
        routes = dfs(paths, new_path, routes)
            
    return routes
    

def add_path(src, dst):
    global paths
    
    if src not in paths:
        paths[src] = []
    if dst not in paths:
        paths[dst] = []
        
    paths[src].append(dst)
    paths[dst].append(src)
        

with open('input.in', 'r') as input_file:
    paths = {}
    
    routes = []
    
    for line in input_file.readlines():
        (src, dst) = line[:-1].split('-')
        
        add_path(src, dst)
        
    
    routes = dfs(paths, ['start'], routes)
    
    print(len(routes))