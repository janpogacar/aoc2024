import numpy as np
from collections import defaultdict
from copy import copy

def flatten_comprehension(matrix):
    return [item for row in matrix for item in row]

# parse input data
input_data = np.loadtxt("input11.txt", dtype="int")

num_dict = defaultdict(int)

for x in input_data:
    num_dict[int(x)] = 1 
result = 0

for cycle in range(75): # Change to 25 for part 1
    dict_copy = copy(num_dict)
    for x in dict_copy:
        if num_dict[x] > 0:
            if int(x) == 0:
                num_dict[1] += dict_copy[x]
                num_dict[x] -= dict_copy[x]
            elif len(str(x)) % 2 == 0:
                string = str(x)
                firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
                num_dict[int(firstpart)] += dict_copy[x]
                num_dict[int(secondpart)] += dict_copy[x]
                num_dict[x] -= dict_copy[x]
            else:
               num_dict[x*2024] += dict_copy[x] 
               num_dict[x] -= dict_copy[x]  

for x in num_dict:
    result += num_dict[x]
zero_data = [0]

print(result)