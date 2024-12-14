import re
from collections import defaultdict

input_file = open("input14.txt", "r")
combs = input_file.read().split("\n")

lines = defaultdict(dict)

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
print(0)
