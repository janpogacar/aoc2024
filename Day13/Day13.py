import re
from collections import defaultdict
import itertools
import numpy as np
input_file = open("input13.txt", "r")
combs = input_file.read().split("\n\n")

input_dict = defaultdict(dict)
for i, comb in enumerate(combs):
    matches = re.findall(r'X\+(\d+),\s*Y\+(\d+)|X=(\d+),\s*Y=(\d+)', comb)
    ax, ay, bx, by, px, py = [int(num) for match in matches for num in match if num]
    input_dict[i]["ax"] = int(ax)
    input_dict[i]["ay"] = int(ay)
    input_dict[i]["bx"] = int(bx)
    input_dict[i]["by"] = int(by)
    input_dict[i]["px"] = int(px)
    input_dict[i]["py"] = int(py)
    input_dict[i]["px_p2"] = int(px)+10000000000000
    input_dict[i]["py_p2"] = int(py)+10000000000000

test = [p for p in itertools.product(list(range(1,101)), repeat=2)]
result = 0
result2 = 0

for dict in input_dict:
    game = input_dict[dict]
    A = np.array([[game["ax"], game["bx"]], [game["ay"], game["by"]]])
    b = np.array([game["px"], game["py"]])
    b2 = np.array([game["px_p2"], game["py_p2"]])
    x = np.linalg.solve(A, b)
    x2 = np.linalg.solve(A, b2)
    n1, n2 = np.round(x).astype('uint64') 
    if (game["ax"]*n1 + game["bx"]*n2 == game["px"]) and (game["ay"]*n1 + game["by"]*n2 == game["py"]):
        result += (n1*3 + n2)
    n1, n2 = np.round(x2).astype('uint64') 
    if (game["ax"]*n1 + game["bx"]*n2 == game["px_p2"]) and (game["ay"]*n1 + game["by"]*n2 == game["py_p2"]):
        result2 += (n1*3 + n2)


print(int(result))
print(int(result2))


print(0)