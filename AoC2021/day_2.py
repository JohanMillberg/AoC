with open("input2.txt") as file:
    input = file.read().splitlines()

def part1(input):
    commands = [(input[n].split()[0], int(input[n].split()[1])) for n in range(len(input))]

    horizontal_pos = 0
    depth = 0

    for command in commands:
        if command[0] == 'forward':
            horizontal_pos += command[1]
        elif command[0] == 'down':
            depth += command[1]
        else:
            depth -= command[1]

    print(horizontal_pos*depth)

def part2(input):
    commands = [(input[n].split()[0], int(input[n].split()[1])) for n in range(len(input))]

    horizontal_pos = 0
    depth = 0
    aim = 0

    for command in commands:
        if command[0] == 'forward':
            horizontal_pos += command[1]
            depth += aim*command[1]
        elif command[0] == 'down':
            aim += command[1]
        else:
            aim -= command[1]

    print(horizontal_pos*depth)

part1(input)

part2(input)