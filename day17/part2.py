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
    
def simulate(vx, vy, x1, x2, y1, y2):
    x,y = 0,0
    
    while True:
        x += vx
        y += vy
        if x > x2 or y < y1:
            return False 
        if x >= x1 and y <= y2:
            return True
        vx -= 1
        if vx < 0:
            vx = 0
        vy -= 1

with open('input.in', 'r') as input_file:
    pattern = r'target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)'
    match = re.match(pattern, input_file.readline())
    x1,x2,y1,y2 = [int(c) for c in match.groups()]
    
    for x in range(x1, x2+1):
        vx_min = get_vx(x)
        if vx_min is not None:
            break
    
    vx_max = x2
    
    vy_max = (y1 * (-1)) + 1
    vy_min = y1
    
    velocities = []
    
    for vx in range(vx_min, vx_max+1):
        for vy in range(vy_min, vy_max+1):
            if simulate(vx,vy, x1, x2, y1, y2):
                velocities.append((vx,vy))
                
    print len(velocities)
    
        