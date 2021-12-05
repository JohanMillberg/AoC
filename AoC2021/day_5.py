import numpy as np

with open("input5.txt") as file:
    input = file.read().splitlines()

def part1(input):
    separated_commands = [[command.split(' -> ')[0], command.split(' -> ')[1]] for command in input]
    x1_s = []
    y1_s = []
    x2_s = []
    y2_s = []
    for command in separated_commands:
        if int(command[0].split(',')[0]) == int(command[1].split(',')[0]) or int(command[0].split(',')[1]) == int(command[1].split(',')[1]):
            x1_s.append(int(command[0].split(',')[0]))
            x2_s.append(int(command[1].split(',')[0]))
            y1_s.append(int(command[0].split(',')[1]))
            y2_s.append(int(command[1].split(',')[1]))

    seafloor_width = max(x1_s+x2_s) + 1
    seafloor_height = max(y1_s+y2_s) + 1

    seafloor = [[0] * seafloor_width for _ in range(seafloor_height)]

    for x1, y1, x2, y2 in zip(x1_s, y1_s, x2_s, y2_s):
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for y_s in range(y1, y2 + 1):
                seafloor[x1][y_s] += 1
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for x_s in range(x1, x2 + 1):
                seafloor[x_s][y1] += 1

    print(len([value for row in seafloor for value in row if value > 1]))

def part2(input):
    separated_commands = [[command.split(' -> ')[0], command.split(' -> ')[1]] for command in input]
    x1_s = []
    y1_s = []
    x2_s = []
    y2_s = []
    for command in separated_commands:
        x1_s.append(int(command[0].split(',')[0]))
        x2_s.append(int(command[1].split(',')[0]))
        y1_s.append(int(command[0].split(',')[1]))
        y2_s.append(int(command[1].split(',')[1]))

    seafloor_width = max(x1_s+x2_s) + 1
    seafloor_height = max(y1_s+y2_s) + 1

    seafloor = [[0] * seafloor_width for _ in range(seafloor_height)]

    for x1, y1, x2, y2 in zip(x1_s, y1_s, x2_s, y2_s):
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for y_s in range(y1, y2 + 1):
                seafloor[x1][y_s] += 1
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for x_s in range(x1, x2 + 1):
                seafloor[x_s][y1] += 1
        else:
            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            incline = (y1-y2) // (x1-x2)
            for x_s in range(x1, x2 + 1):
                y = y1 + incline*(x_s - x1)
                seafloor[x_s][y] += 1

    print(len([value for row in seafloor for value in row if value > 1]))

part1(input)
part2(input)