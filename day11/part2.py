def nonzero(octopodes):
    for row in octopodes:
        for octopus in row:
            if octopus != 0:
                return True
    return False

def process(octopodes):
    for y in range(len(octopodes)):
        for x in range(len(octopodes[y])):
            octopodes[y][x] += 1
    
    changed = True
    while changed:
        changed = False
        
        for y in range(len(octopodes)):
            for x in range(len(octopodes[y])):
                if octopodes[y][x] > 9:
                    changed = True
                    octopodes[y][x] = 0
                    for dy in (-1,0,1):
                        for dx in (-1,0,1):
                            (x2,y2) = (x+dx, y+dy)
                            
                            if x2 >= 0 and x2 < len(octopodes[y]) and y2 >= 0 and y2 < len(octopodes[y]):
                                if octopodes[y2][x2] == 0:
                                    continue
                                else:
                                    octopodes[y2][x2] += 1

    
with open('input.in', 'r') as input_file:
    octopodes = [map(int, list(line[:-1])) for line in input_file.readlines()]
    
    i = 0
    while nonzero(octopodes):
        process(octopodes)
        i += 1
    
    print(i)
