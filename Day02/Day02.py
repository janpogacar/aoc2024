import numpy as np

# parse input data
input_file = open("input_02.txt", "r")  
data = input_file.read()
input_data = data.split("\n") 

result = 0
for x in input_data:
    data_line = list(map(int, x.split(" ")))
    if (sorted(data_line, reverse=True) == data_line) or (sorted(data_line) == data_line): # Check if increasing or decreasing
        if np.all(np.abs(np.diff(data_line)) >= 1) and np.all(np.abs(np.diff(data_line)) <= 3): # Check if within boundaries
            result += 1

print(f"Part 1 solution: {result}")   

# For part two, pop a single element if list does not match criteria. If it does, exit the loop
result = 0
for x in input_data:
    data_line = list(map(int, x.split(" ")))
    data_line2 = data_line.copy()
    for i in range(len(data_line2)+1):
        if (sorted(data_line, reverse=True) == data_line) or (sorted(data_line) == data_line): # Check if increasing or decreasing
            if np.all(np.abs(np.diff(data_line)) >= 1) and np.all(np.abs(np.diff(data_line)) <= 3): # Check if within boundaries
                result += 1
                break
        data_line = data_line2.copy()
        if i < len(data_line2):
            data_line.pop(i)

print(f"Part 2 solution: {result}")  