
with open('input.in', 'r') as input_file:
    count = 0
    for line in input_file.readlines():
        output = line.split('|')[1]
        words = output.split()
        
        for word in words:
            if len(word) in (2, 3, 4, 7):
                count += 1
    print(count)