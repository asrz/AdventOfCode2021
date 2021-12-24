def pad_image(image, char):
    #adds 2 borders of dots
    result = []
    
    blank_row = list(char * (len(image[0]) + 4))
    
    result.append(blank_row)
    result.append(blank_row)
    for row in image:
        result.append([char,char] + row + [char,char])
    result.append(blank_row)
    result.append(blank_row)
    
    return result
    
def count_pixels(image):
    return sum([row.count('#') for row in image])    

def apply_algorithm(input_image, algorithm, char):
    input_image = pad_image(input_image, char)

#     print_image(input_image)
    
    height = len(input_image)
    width = len(input_image[0])
    
    default_char = algorithm[0] if char == '.' else algorithm[-1]
    
    output_image = [list(default_char*width) for _ in range(height)]
    
    for y in range(1, height-1):
        for x in range(1, width-1):
            string = ''
            for dy in (-1,0,1):
                for dx in (-1,0,1):
                    try:
                        string += input_image[y+dy][x+dx]
                    except IndexError as e:
                        print(y, dy, x, dx)
                        print(input_image[y+dy])
                        raise e
            index = int(string.replace('.', '0').replace('#', '1'), 2)
            output_image[y][x] = algorithm[index]
            
    return output_image
            
def print_image(image):
    for row in image:
        print(''.join(row)) 
    print('')           

with open('input.in', 'r') as input_file:
    algorithm = input_file.readline()[:-1]
    input_file.readline()
    
    input_image = [list(line[:-1]) for line in input_file.readlines()]
    
    char = None
    for i in range(50):
        if i == 0:
            char = '.'
        else:
            if char == '.':
                char = algorithm[0]
            else:
                char = algorithm[-1]
            
        
        output_image = apply_algorithm(input_image, algorithm, char)
#         print_image(output_image)
        input_image = output_image
    
    print(count_pixels(output_image))
