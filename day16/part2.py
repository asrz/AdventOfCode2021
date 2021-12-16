import operator

HEX_MAPPING= {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111'
}

def hex_to_binary(word):
    bitstring = ''
    
    for char in list(word):
        bitstring += HEX_MAPPING[char]
        
    return bitstring
    
def decode_packet(string, i):
    bits = hex_to_binary(string)

    version = int(bits[i:i+3], 2)
    i += 3
    
    type_id = int(bits[i:i+3], 2)
    i += 3
    
    if type_id == 4:
        bitstring = ''
        while True:
            group = bits[i:i+5]
            
            bitstring += group[1:]
            
            i += 5
            if group[0] == '0':
                break
            
        number = int(bitstring, 2)
        return i, number
    else:
        length_type_id = bits[i]
        i+= 1
        
        numbers = []
        
        if length_type_id == '0':
            length = int(bits[i:i+15], 2)
            i += 15
            l, number = decode_packet(string, i)
            numbers.append(number)
            while l < i + length:
                l, number = decode_packet(string, l)
                numbers.append(number)
            i = l
        else:
            num_packets = int(bits[i:i+11], 2)
            i += 11
            for _ in range(num_packets):
                i, number = decode_packet(string, i)
                numbers.append(number)
                
        value = None
        
        if type_id == 0:
            value = sum(numbers)
        elif type_id == 1:
            value = reduce(operator.mul, numbers, 1)
        elif type_id == 2:
            value = min(numbers)
        elif type_id == 3:
            value = max(numbers)
        elif type_id == 5:
            value = 1 if numbers[0] > numbers[1] else 0
        elif type_id == 6:
            value = 1 if numbers[0] < numbers[1] else 0
        elif type_id == 7:
            value = 1 if numbers[0] == numbers[1] else 0  
        
        return i, value

with open('input.in', 'r') as input_file:
    for line in input_file.readlines():
        packet = line[:-1]
        i, value = decode_packet(packet, 0)
        print(packet, value)
