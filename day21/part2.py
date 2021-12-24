import re
import time

start = time.time()

rolls = [0 for _ in range(10)]
for a in (1,2,3):
    for b in (1,2,3):
        for c in (1,2,3):
            rolls[a+b+c] += 1
            
print(rolls)

def play(positions, scores, player, universes):
    wins = [0 for _ in range(len(scores))]
    
    for roll, count in enumerate(rolls[3:]):
        roll += 3
        new_positions = positions[:]
        new_scores = scores[:]
        next_player = 3 - player
        new_universes = universes * count
        
        position = positions[player]
        position += roll
        if position > 10:
            position -= 10
        new_scores[player] += position
        new_positions[player] = position
        if new_scores[player] >= 21:
            wins[player] += new_universes
        else:
            next_wins = play(new_positions, new_scores, next_player, new_universes)
        
            for i in range(len(wins)):
                wins[i] += next_wins[i]
    
    return wins
        


with open('input.in', 'r') as input_file:
    line_pattern = r'Player (\d+) starting position: (\d+)'
    positions = [0]
    for line in input_file.readlines():
        match = re.match(line_pattern, line)
        player, space = [int(x) for x in match.groups()]
        positions.append(space)
        
    scores = [0 for _ in range(len(positions))]
    
    wins = play(positions, scores, 1, 1)
 
    print(max(wins))
    print(time.time() - start, 's')
    
    