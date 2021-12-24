import re

with open('test.in', 'r') as input_file:
    
    line_pattern = r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)'
    
    on_cubes = set()
    
    for line in input_file.readlines():
        match = re.match(line_pattern, line)
        state = match.groups()[0]
        x1,x2,y1,y2,z1,z2 = [int(n) for n in match.groups()[1:]] 
        
        x1 = max(x1, -50)
        x2 = min(x2, 50)
        y1 = max(y1, -50)
        y2 = min(y2, 50)
        z1 = max(z1, -50)
        z2 = min(z2, 50)
    
        for x in range(x1,x2+1):
            for y in range(y1, y2+1):
                for z in range(z1, z2+1):
                    cube = (x,y,z)
                    if state == 'on':
                        on_cubes.add(cube)
                    else:
                        if cube in on_cubes:
                            on_cubes.remove(cube)
                            
    print len(on_cubes)