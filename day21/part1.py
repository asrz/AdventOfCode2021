import re
from __builtin__ import True

def roll():
    global rolls, dice
    rolls += 3
    
    result = 3*(dice+1)
    
    dice += 3
    
    if dice > 100:
        result -= (100 * (dice-100))
        dice = dice - 100
        
    return result

with open('input.in', 'r') as input_file:
    line_pattern = r'Player (\d+) starting position: (\d+)'
    positions = [0]
    for line in input_file.readlines():
        match = re.match(line_pattern, line)
        player, space = [int(x) for x in match.groups()]
        positions.append(space)
        
    rolls = 0
    dice = 1
    scores = [0 for _ in range(len(positions))]
    done = False
    while True:
        for player in range(1, len(positions)):
            position = positions[player]
            position += roll()
            while position > 10:
                position -= 10
            scores[player] += position
            positions[player] = position
            
            if scores[player] >= 1000:
                done = True
                break
        if done:
            break
    
    print(min(scores[1:]) * rolls)
            