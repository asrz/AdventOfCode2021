with open('input.in', 'r') as input_file:    
    fishes = [0 for _ in range(9)]
    
    for x in [int(x) for x in input_file.readline().split(',')]:
        fishes[x] += 1
    
    
    for i in range(256):
        fishes_next = [0 for x in range(9)]
        fishes_next[6] = fishes[0]
        fishes_next[8] = fishes[0]
        
        for j in range(1,9):
            fishes_next[j-1] += fishes[j]
        
        fishes = fishes_next
            
             
          
    print(sum(fishes))