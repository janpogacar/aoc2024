from collections import defaultdict

def array_to_complex_defaultdict(matrix):
    global rob_pos
    result = defaultdict(dict)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            complex_key = complex(col, row)
            result[complex_key]['value'] = matrix[row][col]
            #result[complex_key]['nodes'] = []
            if matrix[row][col] == "@":
                rob_pos = complex_key   

    return result

input_file = open("input15_1.txt", "r")
maze = input_file.read().split("\n")

for i, x in enumerate(maze):
    maze[i] = list(x)

pos_dict = array_to_complex_defaultdict(maze) # index array to dict

moves = open("input15_2.txt", "r").read()

for move in moves:
    if move == ">":
        place_found = False
        for i in range(int(rob_pos.real) + 1, len(maze[0])):
            if pos_dict[complex(i, int(rob_pos.imag))]["value"] == ".":
                place_found = True
                place = i
                break
            elif pos_dict[complex(i, int(rob_pos.imag))]["value"]  == "#":
                break
        if place_found:
            for i in range(place, int(rob_pos.real), -1):
               pos_dict[complex(i, int(rob_pos.imag))]["value"]  = pos_dict[complex(i-1, int(rob_pos.imag))]["value"] 
            pos_dict[rob_pos]["value"]  = "."
            rob_pos += 1

    if move == "<":
        place_found = False
        for i in range(int(rob_pos.real) - 1, 0, -1):
            if pos_dict[complex(i, int(rob_pos.imag))]["value"] == ".":
                place_found = True
                place = i
                break
            elif pos_dict[complex(i, int(rob_pos.imag))]["value"]  == "#":
                break
        if place_found:
            for i in range(place, int(rob_pos.real), 1):
               pos_dict[complex(i, int(rob_pos.imag))]["value"]  = pos_dict[complex(i+1, int(rob_pos.imag))]["value"] 
            pos_dict[rob_pos]["value"]  = "."
            rob_pos -= 1

    if move == "v":
        place_found = False
        for i in range(int(rob_pos.imag) + 1, len(maze)):
            if pos_dict[complex(int(rob_pos.real), i)]["value"] == ".":
                place_found = True
                place = i
                break
            elif pos_dict[complex(int(rob_pos.real), i)]["value"]  == "#":
                break
        if place_found:
            for i in range(place, int(rob_pos.imag), -1):
               pos_dict[complex(int(rob_pos.real), i)]["value"]  = pos_dict[complex(int(rob_pos.real), i-1)]["value"] 
            pos_dict[rob_pos]["value"]  = "."
            rob_pos += 1j

    if move == "^":
        place_found = False
        for i in range(int(rob_pos.imag), 0, -1):
            if pos_dict[complex(int(rob_pos.real), i)]["value"] == ".":
                place_found = True
                place = i
                break
            elif pos_dict[complex(int(rob_pos.real), i)]["value"]  == "#":
                break
        if place_found:
            for i in range(place, int(rob_pos.imag), 1):
               pos_dict[complex(int(rob_pos.real), i)]["value"]  = pos_dict[complex(int(rob_pos.real), i+1)]["value"] 
            pos_dict[rob_pos]["value"]  = "."
            rob_pos -= 1j

result = 0
# score calculation
for x in pos_dict:
    if pos_dict[x]["value"] == "O":
        result += (100*x.imag + x.real)

print(result)
print(0)