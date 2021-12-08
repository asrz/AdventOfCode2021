with open('input.in', 'r') as input_file:
    fishes = [int(x) for x in input_file.readline().split(',')]
    
    for i in range(80):
        #print(fishes)
        for j in range(len(fishes)):
            if fishes[j] == 0:
                fishes[j] = 6
                fishes.append(8)
            else:
                fishes[j] -= 1
            
    print(len(fishes))