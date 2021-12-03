from collections import Counter

with open("input3.txt") as file:
    input = file.read().splitlines()

def part1(input):
    bits = {}

    for i in range(len(input[0])):
        bits[i] = [int(input[n][i]) for n in range(len(input))]

    most_common_bits = [max(set(bits[k]), key = bits[k].count) for k in range(len(bits.keys()))]
    least_common_bits = [min(set(bits[k]), key = bits[k].count) for k in range(len(bits.keys()))]

    gamma_bin = "".join([str(bit) for bit in most_common_bits])
    gamma = int(gamma_bin, 2)

    epsilon_bin = "".join([str(bit) for bit in least_common_bits])
    epsilon = int(epsilon_bin, 2)

    print(epsilon*gamma)

def part2(input):

    o2 = ''
    co2 = ''

    input_o2 = input
    for i in range(len(input_o2[0])):
        amount_per_digit = Counter(x[i] for x in input_o2)

        if amount_per_digit['0'] > amount_per_digit['1']:
            input_o2 = [x for x in input_o2 if x[i] == '0']
        else:
            input_o2 = [x for x in input_o2 if x[i] == '1']
        o2 = input_o2[0]

    input_co2 = input
    for i in range(len(input_co2[0])):
        amount_per_digit = Counter(x[i] for x in input_co2)

        if amount_per_digit['0'] > amount_per_digit['1']:
            input_co2 = [x for x in input_co2 if x[i] == '1']
        else:
            input_co2 = [x for x in input_co2 if x[i] == '0']
        if input_co2:
            co2 = input_co2[0]
        else:
            break

    print(int(co2,2)*int(o2,2))

part1(input)
part2(input)