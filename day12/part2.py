def can_visit(path, option):
    if option == 'start':
        return False
    
    if is_small(option) and option in path:
        for cave in set(path):
            if is_small(cave) and path.count(cave) == 2:
                return False
    
    return True
        

def is_small(cave):
    return cave == cave.lower()

def dfs(paths, path, routes):
    curr = path[-1]
    
    if curr == 'end':
        routes.append(path)
        return routes
    
    options = paths[curr]
    
    for option in options:
        if can_visit(path, option):
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
    
    for key in paths:
        paths[key].sort()
    
    routes = dfs(paths, ['start'], routes)
    
    print(len(routes))
