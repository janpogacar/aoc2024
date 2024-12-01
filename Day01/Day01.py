import numpy as np

# parse input data
input_data = np.loadtxt("input_01.txt", delimiter="   ", dtype="int32")

t_input_data = np.transpose(input_data)
t_input_data[0] = np.sort(t_input_data[0])
t_input_data[1] = np.sort(t_input_data[1])

result01 = 0

for i,x in enumerate(t_input_data[0]):
    result01 += abs(t_input_data[0][i] - t_input_data[1][i])  

print(f"Part 1 solution: {result01}")

# create dict of unique second column values
unique, counts = np.unique(t_input_data[1], return_counts=True)
s_c_values = dict(zip(unique, counts))

result02 = 0
for x in t_input_data[0]:
    if x in t_input_data[1]: # need to check if dict value exists
        result02 += x*s_c_values[x] 

print(f"Part 2 solution: {result02}")