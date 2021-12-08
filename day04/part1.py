
def get_score(board, numbers):
    total = 0
    for row in board:
        for num in row:
            if num not in numbers:
                total += num
    return total * int(numbers[-1])

def is_winner(board, numbers):
    for row in board:
        matches = True    
        for num in row:
            if num not in numbers:
                matches = False
        if matches:
            return True
    for i in range(5):
        matches = True
        for row in board:
            num = row[i]
            if num not in numbers:
                matches = False
        if matches:
            return True
    return False


with open('input.in', 'r') as input_file:
    numbers = [int(x) for x in input_file.readline()[:-1].split(',')]
    
    boards = []
    
    while True:
        line = input_file.readline() #blank
        if line == '':
            break #EOF
        board = []
        for j in range(5):
            row = [int(x) for x in input_file.readline()[:-1].split()]
            board.append(row)
        boards.append(board)
    
    print boards[-1]

    min_count = len(numbers)+1
    score = 0
    for board in boards:
        winner = False
        for i in range(5, len(numbers)):
            if is_winner(board, numbers[:i]):
                if i < min_count:
                    min_count = i
                    score = get_score(board, numbers[:i])
                break
    
    print(score)
                