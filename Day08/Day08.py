from collections import defaultdict
from itertools import combinations
import cmath

input_file = open("input08.txt", "r")  
lines = input_file.read().split("\n")

ant = defaultdict(list)

for imag, line in enumerate(lines):
    for real, char in enumerate(line):
        if char != ".":
            ant[char].append(complex(real,imag))

antinodes = set()

for x in list(ant.keys()):
    pairs = list(combinations(ant[x], 2))
    for pair in pairs:
        d = pair[0]-pair[1]
        z1 = pair[0]+d
        z2 = pair[1]-d
        if (0 <= z1.imag < len(lines)) and (0 <= z1.real < len(lines[0])):
            antinodes.add(z1)
        if (0 <= z2.imag < len(lines)) and (0 <= z2.real < len(lines[0])):
            antinodes.add(z2)

print(len(antinodes))

antinodes2 = set()
for x in list(ant.keys()):
    pairs = list(combinations(ant[x], 2))
    for pair in pairs:
        d = pair[0]-pair[1]
        mul = 0
        while(True):
            z1 = pair[0]+d*mul
            if (0 <= z1.imag < len(lines)) and (0 <= z1.real < len(lines[0])):
                antinodes2.add(z1)
            else:
                break
            mul += 1

        mul = 0
        while(True):
            z2 = pair[1]-d*mul
            if (0 <= z2.imag < len(lines)) and (0 <= z2.real < len(lines[0])):
                antinodes2.add(z2)
            else:
                break
            mul += 1

print(len(antinodes2))