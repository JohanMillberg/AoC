with open("input3.txt") as file:
    input = file.read().splitlines()

def part1(input):
    bits = {}
    for i in range(len(input[0])):
        bits[i] = [int(input[n][i]) for n in range(len(input))]

    gamma = 0
    epsilon = 0
    print(bits)

part1(input)