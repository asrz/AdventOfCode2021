import itertools

def apply_mapping(word, mapping):
    new_word = ''
    for char in list(word):
        new_word += mapping[char]
    return new_word
            
def find_combo(all_words):
    for combo in itertools.permutations(list('abcdefg'), 7):
        mapping = {}
        for i in range(7):
            mapping[list('abcdefg')[i]] = combo[i]
        
        matches = True
        for word in all_words:
            new_word = apply_mapping(word, mapping)
            if set(new_word) not in ACCEPTABLE_WORDS:
                matches = False
                break
        
        if matches:
            return mapping

ACCEPTABLE_WORDS = [set(word) for word in ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']]

with open('input.in', 'r') as input_file:
    
    total = 0
    
    for line in input_file.readlines():
        (words, output_words) = [part.split() for part in line.split('|')]
        
        all_words = words[:]
        all_words.extend(output_words)    

        mapping = find_combo(all_words)
        
        num_str = ''
        
        for word in output_words:
            new_word = apply_mapping(word, mapping)
            digit = ACCEPTABLE_WORDS.index(set(new_word))
            num_str += str(digit)
        
        total += int(num_str)
    print(total)