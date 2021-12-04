import numpy as np

class BingoNumber:
    def __init__(self, value):
        self.value = value
        self.is_activated = False

    def __str__(self):
        return self.value

    def activate_number(self):
        self.is_activated = True

with open("input4.txt") as file:
    input = file.read().splitlines()

def part_1(input):
    bingo_numbers = [int(num) for num in input[0].split(',')]
    input.pop(0)
    boards = []
    found = False

    for index, line in enumerate(input):
        if line == '':
            board = np.array([[float(num) for num in input[i].split(' ') if num != ''] for i in range(index+1, index+6)])
            boards.append(board)

    winning_index = []

    for bingo_number in bingo_numbers:

        for index, board in enumerate(boards):
            if index in winning_index:
                continue
            board[board == bingo_number] = np.nan
            for i in range(board.shape[0]):
                if False not in np.isnan(board[i,:]) or False not in np.isnan(board[:,i]):
                    print(board)
                    print(np.nansum(board)*bingo_number)
                    winning_index.append(index)
                    found = True



part_1(input)

