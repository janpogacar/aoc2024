import re
from collections import defaultdict
import numpy as np
from matplotlib import pyplot

input_file = open("input14.txt", "r")
combs = input_file.read().split("\n")

lines = defaultdict(dict)
lines2 = defaultdict(dict) # for part 2

size_x = 101
size_y = 103
num = 100
q1 = 0
q2 = 0
q3 = 0
q4 = 0

for i, line in enumerate(combs):
    p, v = line.split(" ")
    px, py = p[2:].split(",")
    vx, vy = v[2:].split(",")

    lines[i]["px"] = int(px) 
    lines[i]["py"] = int(py) 
    lines[i]["vx"] = int(vx) 
    lines[i]["vy"] = int(vy)

    lines2[i]["px"] = int(px) 
    lines2[i]["py"] = int(py) 
    lines2[i]["vx"] = int(vx) 
    lines2[i]["vy"] = int(vy)

    lines[i]["px"] = (lines[i]["px"]+lines[i]["vx"]*num) %  size_x
    if lines[i]["px"] < 0:
        lines[i]["px"] += size_x

    lines[i]["py"] = (lines[i]["py"]+lines[i]["vy"]*num) %  size_y
    if lines[i]["py"] < 0:
        lines[i]["py"] += size_y

    if lines[i]["px"] < (size_x/2 -1) and lines[i]["py"] < (size_y/2 -1):
        q1 += 1
    elif lines[i]["px"] < (size_x/2 -1) and lines[i]["py"] > (size_y/2):
        q3 += 1
    elif lines[i]["px"] > (size_x/2) and lines[i]["py"] < (size_y/2 -1):
        q2 += 1
    elif lines[i]["px"] > (size_x/2) and lines[i]["py"] > (size_y/2):
        q4 += 1

print(q1*q2*q3*q4)

p2_list = []
# for part 2, find low coordinate variance
for n in range(1, 10000):
    tmp_x = []
    tmp_y = []
    for i in range(len(lines2)):
        lines2[i]["px"] = (lines2[i]["px"]+lines2[i]["vx"]) %  size_x
        if lines2[i]["px"] < 0:
            lines2[i]["px"] += size_x
        tmp_x.append(lines2[i]["px"])

        lines2[i]["py"] = (lines2[i]["py"]+lines2[i]["vy"]) %  size_y
        if lines2[i]["py"] < 0:
            lines2[i]["py"] += size_y
        tmp_y.append(lines2[i]["py"])
    p2_list.append([n,np.var(tmp_x)+np.var(tmp_y)]) 
           

np_p2 = np.array(p2_list)
np_p2_sorted = np_p2[:,1].argsort()
print(np_p2_sorted[0]+1)