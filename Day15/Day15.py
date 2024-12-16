from collections import defaultdict
import numpy as np

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

def array_to_complex_defaultdict_p2(matrix):
    global rob_pos
    result = defaultdict(dict)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            complex_key = complex(col, row)
            if matrix[row][col] == "#":
                result[complex(2*col, row)]['value'] = "#"
                result[complex(2*col+1, row)]['value'] = "#"
            if matrix[row][col] == "O":
                result[complex(2*col, row)]['value'] = "["
                result[complex(2*col+1, row)]['value'] = "]" 
            if matrix[row][col] == ".":
                result[complex(2*col, row)]['value'] = "."
                result[complex(2*col+1, row)]['value'] = "."
            if matrix[row][col] == "@":
                result[complex(2*col, row)]['value'] = "@"
                result[complex(2*col+1, row)]['value'] = "."
                rob_pos = complex(2*col, row)   
        
    return result

def move_box_up(x1, x2, y):
    # Check if anything is blocking the box
    if pos_dict[complex(x1, y-1)]["value"]  == "#" or pos_dict[complex(x2, y-1)]["value"]  == "#":
        box_moved = False
    elif pos_dict[complex(x1, y-1)]["value"]  == "." and pos_dict[complex(x2, y-1)]["value"]  == ".":
        box_moved = True
    elif (pos_dict[complex(x1, y-1)]["value"] == "[") and (pos_dict[complex(x2, y-1)]["value"] == "]"): # Single box above
        box_moved = move_box_up(x1, x2, y-1)
    elif (pos_dict[complex(x1, y-1)]["value"] == "]") and (pos_dict[complex(x2, y-1)]["value"] == "."):
        if [x1-1, x1, y-1] not in box_to_move:
            box_moved = move_box_up(x1-1, x1, y-1)
        else:
            box_moved = True
    elif (pos_dict[complex(x1, y-1)]["value"] == ".") and (pos_dict[complex(x2, y-1)]["value"] == "["):
        if [x2, x2-1, y-1] not in box_to_move:
            box_moved = move_box_up(x2, x2+1, y-1)
        else:
            box_moved = True 
    elif (pos_dict[complex(x1, y-1)]["value"] == "]") and (pos_dict[complex(x2, y-1)]["value"] == "["):
        if [x1-1, x1, y-1] not in box_to_move:
            bm1 = (move_box_up(x1-1, x1, y-1))
        else:
            bm1 = True
        if [x2, x2+1, y-1] not in box_to_move:
            bm2 = (move_box_up(x2, x2+1, y-1))
        else:
            bm2 = True 
        box_moved = bm1 and bm2 
    if box_moved: # TODO: box moves need to be in unison!!
        box_to_move.append([x1, x2, y])
    return box_moved     

def move_box_down(x1, x2, y):
    # Check if anything is blocking the box
    if pos_dict[complex(x1, y+1)]["value"]  == "#" or pos_dict[complex(x2, y+1)]["value"]  == "#":
        box_moved = False
    elif pos_dict[complex(x1, y+1)]["value"]  == "." and pos_dict[complex(x2, y+1)]["value"]  == ".":
        box_moved = True
    elif (pos_dict[complex(x1, y+1)]["value"] == "[") and (pos_dict[complex(x2, y+1)]["value"] == "]"): # Single box above
        box_moved = move_box_down(x1, x2, y+1)
    elif (pos_dict[complex(x1, y+1)]["value"] == "]") and (pos_dict[complex(x2, y+1)]["value"] == "."):
        if [x1-1, x1, y+1] not in box_to_move:
            box_moved = move_box_down(x1-1, x1, y+1)
        else:
            box_moved = True
    elif (pos_dict[complex(x1, y+1)]["value"] == ".") and (pos_dict[complex(x2, y+1)]["value"] == "["):
        if [x2, x2+1, y+1] not in box_to_move:
            box_moved = move_box_down(x2, x2+1, y+1)
        else:
            box_moved = True 
    elif (pos_dict[complex(x1, y+1)]["value"] == "]") and (pos_dict[complex(x2, y+1)]["value"] == "["): 
        if [x1-1, x1, y+1] not in box_to_move:
            bm1 = (move_box_down(x1-1, x1, y+1))
        else:
            bm1 = True
        if [x2, x2+1, y+1] not in box_to_move:
            bm2 = (move_box_down(x2, x2+1, y+1))
        else:
            bm2 = True 
        box_moved = bm1 and bm2 
    if box_moved:
        box_to_move.append([x1, x2, y])
    return box_moved  

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
maze2 = np.zeros([len(maze), 2*len(maze[0])], str)
pos_dict = array_to_complex_defaultdict_p2(maze) # index array to dict

for dbg, move in enumerate(moves):
    box_to_move = []
    if move == ">":
        place_found = False
        for i in range(int(rob_pos.real) + 1, 2*len(maze[0])):
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
        if pos_dict[complex(int(rob_pos.real), int(rob_pos.imag+1))]["value"] == ".":
            place_found = True
        elif pos_dict[complex(int(rob_pos.real), int(rob_pos.imag+1))]["value"]  == "]":
            box_to_move = []
            place_found = move_box_down(int(rob_pos.real)-1, int(rob_pos.real), int(rob_pos.imag)+1)
        elif pos_dict[complex(int(rob_pos.real), int(rob_pos.imag+1))]["value"]  == "[":
            box_to_move = []
            place_found = move_box_down(int(rob_pos.real), int(rob_pos.real)+1, int(rob_pos.imag)+1)
        elif pos_dict[complex(int(rob_pos.real), int(rob_pos.imag+1))]["value"]  == "#":
            place_found = False

        if place_found:
            for x1, x2, y in box_to_move:
                pos_dict[complex(x1, y+1)]["value"] = "["
                pos_dict[complex(x2, y+1)]["value"] = "]"
                pos_dict[complex(x1, y)]["value"] = "."
                pos_dict[complex(x2, y)]["value"] = "."

            pos_dict[rob_pos]["value"]  = "."
            rob_pos += 1j
            pos_dict[rob_pos]["value"]  = "@"

    if move == "^":
        place_found = False
        if pos_dict[complex(int(rob_pos.real), int(rob_pos.imag-1))]["value"] == ".":
            place_found = True
        elif pos_dict[complex(int(rob_pos.real), int(rob_pos.imag-1))]["value"]  == "]":
            box_to_move = []
            place_found = move_box_up(int(rob_pos.real)-1, int(rob_pos.real), int(rob_pos.imag)-1)
        elif pos_dict[complex(int(rob_pos.real), int(rob_pos.imag-1))]["value"]  == "[":
            box_to_move = []
            place_found = move_box_up(int(rob_pos.real), int(rob_pos.real)+1, int(rob_pos.imag)-1)
        elif pos_dict[complex(int(rob_pos.real), int(rob_pos.imag-1))]["value"]  == "#":
            place_found = False

        if place_found:
            for x1, x2, y in box_to_move:
                pos_dict[complex(x1, y-1)]["value"] = "["
                pos_dict[complex(x2, y-1)]["value"] = "]"
                pos_dict[complex(x1, y)]["value"] = "."
                pos_dict[complex(x2, y)]["value"] = "."

            pos_dict[rob_pos]["value"]  = "."
            rob_pos -= 1j
            pos_dict[rob_pos]["value"]  = "@"
    # f = open("out.txt", "a")
    # f.write(str(dbg) + "\n")
    # f.write(str(move) + "\n")
    # for x in pos_dict:
    #     maze2[int(x.imag)][int(x.real)] = pos_dict[x]["value"]
    # #f.write(str(maze2))
    # f.write("\n")
    # f.close()
    # np.savetxt("out.txt", maze2, fmt="%s")
         

result = 0
# score calculation
for x in pos_dict:
    if pos_dict[x]["value"] == "[":
        result += (100*x.imag + x.real)

print(result)
print(0)