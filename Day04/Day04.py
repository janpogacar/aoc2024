import numpy as np
from collections import defaultdict

input_file = open("input04.txt", "r")  
data = input_file.read().split("\n")

# Pad data to allow for easier searching
for i in range(len("XMAS")):
    data.insert(0, "." * len(data[0]))
    data.append("." * len(data[0]))

for i, x in enumerate(data):
    ldata = list(data[i])
    for j in range(len("XMAS")):
        ldata.insert(0, ".")
        ldata.append(".")
    data[i] = ldata

tdata = np.transpose(data)
result = 0
for i in range(len(data)-4):
    for j in range(len(data[0])-4):
        # Check left to right
        if "".join(data[i][j:j+4]) == "XMAS":
            result += 1
        # Check right to left
        if "".join(data[i][j:j+4])[::-1] == "XMAS":
            result += 1
        # Check top to bottom
        if "".join(tdata[i][j:j+4]) == "XMAS":
            result += 1
        # Check bottom to top
        if "".join(tdata[i][j:j+4])[::-1] == "XMAS":
            result += 1
        diag_list = []
        diag_list2 = []
        for k in range(len("XMAS")):
            diag_list.append(data[i+k][j+k])
            diag_list2.append(data[i-k][j+k])
        
        # Check ld
        if "".join(diag_list2[::-1]) == "XMAS":
            result += 1
        # Check rd
        if "".join(diag_list) == "XMAS":
            result += 1
        
        # Check ru
        if "".join(diag_list2) == "XMAS":
            result += 1
        # Check lu
        if "".join(diag_list[::-1]) == "XMAS":
            result += 1

print(result)

mas_list = [[list("M_M"),list("_A_"), list("S_S")], [list("S_M"), list("_A_"), list("S_M")], [list("S_S"), list("_A_"), list("M_M")], [list("M_S"), list("_A_"), list("M_S")]]

result = 0
for i in range(len(data)-4):
    for j in range(len(data[0])-4):
        test_list = []
        for k in range(3):
            test_list.append(data[i+k][j:j+3])
        for x in mas_list:
            if np.count_nonzero(np.array(test_list) == np.array(x)) == 5:
                result += 1
            
print(result)
