import re
import math
import itertools

def get_distance(beacon1, beacon2):
    (x1,y1,z1) = beacon1
    (x2,y2,z2) = beacon2
    
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    dz = abs(z1 - z2)
    
    return math.sqrt(dx**2 + dy**2 + dz**2)
    
def get_beacon_distances(beacons, scanner):
    beacon_distances = []
    for i in range(len(beacons[scanner])):
        beacon_distances.append([])
        for j in range(i+1, len(beacons[scanner])):
            beacon1 = beacons[scanner][i]
            beacon2 = beacons[scanner][j]
            
            distance = get_distance(beacon1, beacon2)
            beacon_distances[-1].append(distance)
            
    return beacon_distances

def find_matches(beacon_distances1, beacon_distances2):
    flat_beacon_distances1 = set(flatten(beacon_distances1))
    flat_beacon_distances2 = set(flatten(beacon_distances2))
    
    return flat_beacon_distances1.intersection(flat_beacon_distances2)

def flatten(metalist):
    result = []
    for sublist in metalist:
        result.extend(sublist)
        
    return result

def find_scanner(scanner1, scanner2, beacons, beacon_distances, scanners):
    candidates = set()
    
    for i in range(len(beacon_distances[scanner2])):
        for j in range(len(beacon_distances[scanner2][i])):
            distance2 = beacon_distances[scanner2][i][j]
            for k in range(len(beacon_distances[scanner1])):
                for l in range(len(beacon_distances[scanner1][k])):
                    distance1 = beacon_distances[scanner1][k][l]
                    if distance2 == distance1:
                        beacon1a = beacons[scanner1][k]
                        beacon1b = beacons[scanner1][k+l+1]
                        beacon2a = beacons[scanner2][i]
                        beacon2b = beacons[scanner2][i+j+1]
                        
                        for args in ((beacon1a, beacon1b, beacon2a, beacon2b), (beacon1a, beacon1b, beacon2b, beacon2a)):
                            result = solve(*args)
                            if result is not None:
                                candidate, transform_vector = result
                                if candidate in candidates:
                                    return candidate, transform_vector
                                else:
                                    candidates.add(candidate)


def transform(vector, transform_vector):
    x = vector[abs(transform_vector[0])-100]
    y = vector[abs(transform_vector[1])-100]
    z = vector[abs(transform_vector[2])-100]
    
    if transform_vector[0] < 0:
        x *= -1
    if transform_vector[1] < 0:
        y *= -1
    if transform_vector[2] < 0:
        z *= -1
    
    return (x,y,z)

def get_transform_vector(vector1, vector2):
    transform_vector = [0, 0, 0]
    
    for a in range(3):
        for b in range(3):
            if vector2[a] == vector1[b]:
                transform_vector[b] = a+100
            elif vector2[a] == -vector1[b]:
                transform_vector[b] = -(a+100)
                
    if transform_vector == [0,0,0]:
        #2 different triples resulted in the same distance
        return None            
    
    return tuple(transform_vector)

def solve(beacon1a, beacon1b, beacon2a, beacon2b):
    distances1 = subtract_vectors(beacon1a, beacon1b)
    distances2 = subtract_vectors(beacon2a, beacon2b)
    
    if 0 in distances1:
        return None #we can't get direction if there's a 0
    if len(set(distances1)) < 3:
        return None #we can't get direction if two axes are the same
    
    transform_vector = get_transform_vector(distances1, distances2)
    if transform_vector is None:
        return None
    
    transformed_beacon2a = transform(beacon2a, transform_vector)
    
    return subtract_vectors(beacon1a, transformed_beacon2a), transform_vector
    

def add_vectors(vector1, vector2):
    (x1,y1,z1) = vector1
    (x2,y2,z2) = vector2
    
    return (x1+x2, y1+y2, z1+z2)

def subtract_vectors(vector1, vector2):
    (x1,y1,z1) = vector1
    (x2,y2,z2) = vector2
    
    return (x1-x2, y1-y2, z1-z2)

def get_manhattan(vector1, vector2):
    (x1,y1,z1) = vector1
    (x2,y2,z2) = vector2
    
    return abs(x1-x2) + abs(y1-y2) + abs(z1-z2)

with open('input.in', 'r') as input_file:
    scanner_pattern = r'--- scanner (\d+) ---'
    beacon_pattern = r'(-?\d+),(-?\d+),(-?\d+)'
    
    beacons = {}
    
    scanner = None
    for line in input_file.readlines():
        match = re.match(beacon_pattern, line)
        if match is None:
            match = re.match(scanner_pattern, line)
            if match is None:
                continue
            scanner = int(match.groups()[0])
            beacons[scanner] = []
            continue
            
        (x,y,z) = map(int, match.groups())
        beacons[scanner].append((x,y,z))
        
    beacon_distances = {}
    
    for scanner in beacons:
        beacon_distances[scanner] = get_beacon_distances(beacons, scanner)
        
    scanners = { 0: (0,0,0) }
    
    while len(scanners) < len(beacons):
        for scanner2 in beacons:
            if scanner2 in scanners:
                continue
            for scanner1 in scanners:
                matches = find_matches(beacon_distances[scanner1], beacon_distances[scanner2])
                if len(matches) < 12:
                    continue
                else:
                    (scanner_location, transform_vector) = find_scanner(scanner1, scanner2, beacons, beacon_distances, scanners)
                    scanners[scanner2] = scanner_location
                    
                    for i in range(len(beacons[scanner2])):
                        beacons[scanner2][i] = add_vectors(scanner_location, transform(beacons[scanner2][i], transform_vector))
                    
                    break
        
    print 'part1', len(set(flatten(beacons.values())))
    
    max_manhattan = 0    
    for (a,b) in itertools.combinations(range(len(scanners)), 2):
        max_manhattan = max(max_manhattan, get_manhattan(scanners[a], scanners[b]))
    print 'part2', max_manhattan
