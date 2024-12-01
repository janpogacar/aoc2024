import numpy as np

# parse input data
input_data = np.loadtxt("input_01.txt", dtype="int32")

t_input_data = np.transpose(input_data)
t_input_data.sort(axis=1)

result01 = np.sum(np.abs(t_input_data[0] - t_input_data[1]))
print(f"Part 1 solution: {result01}")

result02 = 0
for x in t_input_data[0]:
    result02 += x*list(t_input_data[1]).count(x)

print(f"Part 2 solution: {result02}")