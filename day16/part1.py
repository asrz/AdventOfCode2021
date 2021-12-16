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
    
def decode_packet(string, i, total_version):
#     print('decoding packet starting at index', i)
    
    bits = hex_to_binary(string)

    version = int(bits[i:i+3], 2)
    total_version += version
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
        return i, total_version
    else:
        length_type_id = bits[i]
        i+= 1
        
        if length_type_id == '0':
            length = int(bits[i:i+15], 2)
            i += 15
            l, total_version = decode_packet(string, i, total_version)
            while l < i + length:
                l, total_version = decode_packet(string, l, total_version)
            return l, total_version
        else:
            num_packets = int(bits[i:i+11], 2)
            i += 11
            for _ in range(num_packets):
                i, total_version = decode_packet(string, i, total_version)
            return i, total_version

with open('input.in', 'r') as input_file:
    packet = input_file.readline()[:-1]
    i, total_version = decode_packet(packet, 0, 0)
    print(total_version)