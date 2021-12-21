import re

def triangle(n):
    return (n * (n+1)) / 2

def get_vx(x):
    vx = 1
    x_max = triangle(vx)
    while x_max < x:
        vx += 1
        x_max = triangle(vx)
    if x_max == x:
        return vx
    return None
    


with open('input.in', 'r') as input_file:
    pattern = r'target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)'
    match = re.match(pattern, input_file.readline())
    x1,x2,y1,y2 = [int(c) for c in match.groups()]
    
    y_maxes = []
    
    for x in range(x1,x2+1):
        vx = get_vx(x)
        if vx is None:
            continue
        vy = (y1 * (-1))-1
        
        y_max = triangle(vy)
        y_maxes.append(y_max)
    
    print(max(y_maxes))
        