with open("input6.txt") as file:
    input = file.read().splitlines()

def part1(input):
    input = input[0].split(',')
    input = [int(fish) for fish in input]

    for i in range(80):
        for k in range(len(input)-1, -1, -1):
            if input[k] == 0:
                input.append(8)
                input[k] = 6
            else:
                input[k] -= 1

    print(len(input))

def part2(input):
    input = input[0].split(',')
    input = [int(fish) for fish in input]
    fish_count = [0]*9

    for fish in input:
        fish_count[fish] += 1
    for i in range(256):
        fish_count.append(fish_count.pop(0))
        fish_count[6] += fish_count[8]
    print(sum(fish_count))
part1(input)
part2(input)
