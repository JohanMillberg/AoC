from collections import defaultdict
import math as m
import numpy as np

with open("input7.txt") as file:
    input = file.read().splitlines()
    input = input[0].split(',')
    input = [int(position) for position in input]

def median(input):
    n = len(input)
    s = sorted(input)
    return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None

def part1(input):
    median_position = median(input)
    differences = [abs(position - median_position) for position in input]

    print(sum(differences))

def part2(input):
    best_position = m.floor(np.mean(input))
    fuel_per_crab = []
    for i in range(len(input)):
        fuel = 0
        for j in range(1,abs(input[i]-best_position)+1):
            fuel += j
        fuel_per_crab.append(fuel)
    print(sum(fuel_per_crab))

part1(input)
part2(input)
