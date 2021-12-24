import re
import time

start = time.time()

class Cuboid:
    def __init__(self, x1,x2,y1,y2,z1,z2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        
    def overlaps(self, other):
        if (self.x2 < other.x1 or self.x1 > other.x2) \
            or (self.y2 < other.y1 or self.y1 > other.y2) \
            or (self.z2 < other.z1 or self.z1 > other.z2):
            return False
        return True

    def __str__(self):
        return str((self.x1,self.x2,self.y1,self.y2,self.z1,self.z2))

    def volume(self):
        return (self.x2 - self.x1 + 1) * (self.y2 - self.y1 + 1) * (self.z2 - self.z1 + 1)

    def intersect(self, other):
        x_min = max(self.x1, other.x1)
        x_max = min(self.x2, other.x2)
        y_min = max(self.y1, other.y1)
        y_max = min(self.y2, other.y2)
        z_min = max(self.z1, other.z1)
        z_max = min(self.z2, other.z2)
        
        return Cuboid(x_min, x_max, y_min, y_max, z_min, z_max)
        
    def __sub__(self, other):
        cuboids = []
        
        x_low = self.x1 < other.x1
        x_high = self.x2 > other.x2
        y_low = self.y1 < other.y1
        y_high = self.y2 > other.y2
        z_low = self.z1 < other.z1
        z_high = self.z2 > other.z2
        
        x_min = max(self.x1, other.x1)
        x_max = min(self.x2, other.x2)
        y_min = max(self.y1, other.y1)
        y_max = min(self.y2, other.y2)
        z_min = max(self.z1, other.z1)
        z_max = min(self.z2, other.z2)
        
        if x_low and y_low and z_low:
            cuboids.append(Cuboid(self.x1, other.x1-1, self.y1, other.y1-1, self.z1, other.z1-1))
        if x_low and y_low and z_high:
            cuboids.append(Cuboid(self.x1, other.x1-1, self.y1, other.y1-1, other.z2+1, self.z2))
        if x_low and y_high and z_low:
            cuboids.append(Cuboid(self.x1, other.x1-1, other.y2+1, self.y2, self.z1, other.z1-1))
        if x_low and y_high and z_high:
            cuboids.append(Cuboid(self.x1, other.x1-1, other.y2+1, self.y2, other.z2+1, self.z2))
        if x_high and y_low and z_low:
            cuboids.append(Cuboid(other.x2+1, self.x2, self.y1, other.y1-1, self.z1, other.z1-1))
        if x_high and y_low and z_high:
            cuboids.append(Cuboid(other.x2+1, self.x2, self.y1, other.y1-1, other.z2+1, self.z2))
        if x_high and y_high and z_low:
            cuboids.append(Cuboid(other.x2+1, self.x2, other.y2+1, self.y2, self.z1, other.z1-1))
        if x_high and y_high and z_high:
            cuboids.append(Cuboid(other.x2+1, self.x2, other.y2+1, self.y2, other.z2+1, self.z2))
        
        if x_low and y_low:
            cuboids.append(Cuboid(self.x1, other.x1-1, self.y1, other.y1-1, z_min, z_max))
        if x_low and y_high:
            cuboids.append(Cuboid(self.x1, other.x1-1, other.y2+1, self.y2, z_min, z_max))
        if x_high and y_low:
            cuboids.append(Cuboid(other.x2+1, self.x2, self.y1, other.y1-1, z_min, z_max))
        if x_high and y_high:
            cuboids.append(Cuboid(other.x2+1, self.x2, other.y2+1, self.y2, z_min, z_max))
            
        if x_low and z_low:
            cuboids.append(Cuboid(self.x1, other.x1-1, y_min, y_max, self.z1, other.z1-1))
        if x_low and z_high:
            cuboids.append(Cuboid(self.x1, other.x1-1, y_min, y_max, other.z2+1, self.z2))
        if x_high and z_low:
            cuboids.append(Cuboid(other.x2+1, self.x2, y_min, y_max, self.z1, other.z1-1))
        if x_high and z_high:
            cuboids.append(Cuboid(other.x2+1, self.x2, y_min, y_max, other.z2+1, self.z2))
            
        if y_low and z_low:
            cuboids.append(Cuboid(x_min, x_max, self.y1, other.y1-1, self.z1, other.z1-1))
        if y_low and z_high:
            cuboids.append(Cuboid(x_min, x_max, self.y1, other.y1-1, other.z2+1, self.z2))
        if y_high and z_low:
            cuboids.append(Cuboid(x_min, x_max, other.y2+1, self.y2, self.z1, other.z1-1))
        if y_high and z_high:
            cuboids.append(Cuboid(x_min, x_max, other.y2+1, self.y2, other.z2+1, self.z2))
        
        if x_low:
            cuboids.append(Cuboid(self.x1, other.x1-1, y_min, y_max, z_min, z_max))
        if x_high:
            cuboids.append(Cuboid(other.x2+1, self.x2, y_min, y_max, z_min, z_max))
        if y_low:
            cuboids.append(Cuboid(x_min, x_max, self.y1, other.y1-1, z_min, z_max))
        if y_high:
            cuboids.append(Cuboid(x_min, x_max, other.y2+1, self.y2, z_min, z_max))
        if z_low:
            cuboids.append(Cuboid(x_min, x_max, y_min, y_max, self.z1, other.z1-1))
        if z_high:
            cuboids.append(Cuboid(x_min, x_max, y_min, y_max, other.z2+1, self.z2))
            
        return cuboids
    
with open('input.in', 'r') as input_file:
        
    line_pattern = r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)'
        
    on_cuboids = []
        
    i = 0
    for line in input_file.readlines():
        i+= 1
        match = re.match(line_pattern, line)
        state = match.groups()[0]
           
        cuboids = [Cuboid(*[int(n) for n in match.groups()[1:]])]
#         print(cuboids[0])
        next_cuboids = []
        to_remove = []
        
        if state == 'on':
            while len(cuboids) > 0:
                for cuboidA in cuboids:
                    for cuboidB in on_cuboids:
                        if cuboidA.overlaps(cuboidB):
                            to_remove.append(cuboidA)
                            next_cuboids.extend(cuboidA - cuboidB)
                            break
                for cuboid in to_remove:
                    cuboids.remove(cuboid)
                on_cuboids.extend(cuboids)
                cuboids = next_cuboids
                to_remove = []
                next_cuboids = []
        if state == 'off':
            for cuboidA in cuboids:
                for cuboidB in on_cuboids:
                    if cuboidA.overlaps(cuboidB):
                        to_remove.append(cuboidB)
                        next_cuboids.extend(cuboidB - cuboidA)
                for cuboid in to_remove:
                    on_cuboids.remove(cuboid)
                on_cuboids.extend(next_cuboids)
          
    print(sum([cuboid.volume() for cuboid in on_cuboids]))


print(time.time() - start)