with open("input1.txt") as file:
    input = file.read().splitlines()

input_list = [int(n) for n in input]

increases = [input_list[n] for n in range(len(input_list)) if input_list[n] > input_list[n-1]]

sliding_window = [input_list[n] + input_list[n+1] + input_list[n+2] for n in range(len(input_list)-2)]
increase_sliding = [sliding_window[n] for n in range(len(sliding_window)) if sliding_window[n] > sliding_window[n-1]]

print(len(increases))
print(len(increase_sliding))