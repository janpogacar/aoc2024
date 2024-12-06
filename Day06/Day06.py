import numpy as np

# parse input data
input_file = open("input06.txt", "r")  
maze = input_file.read().split("\n")
for i, x in enumerate(maze):
    maze[i] = list(x)

np_maze = np.array(maze)
pos = list(zip(*np.where(np_maze == "^")))[0]
pos = list(pos)
start_pos = pos.copy()

dirs = ["up", "right", "down", "left"]
dir = "up"

visited = set()
visited.add(f"{pos[0]},{pos[1]}")

result = 0
while(True): # we will break when we find a path out
    if dir == "up":
        dir_path = np_maze.T[pos[1]][:pos[0]][::-1]
        if "#" not in dir_path:
            for i in range(pos[0], -1, -1):
                visited.add(f"{i},{pos[1]}")
            break
        pos[0] -= np.where(dir_path == "#")[0][0]
        dir = "right"
        for i in range(pos[0], pos[0]+np.where(dir_path == "#")[0][0]+1):
            visited.add(f"{i},{pos[1]}")
    elif dir == "right":
        dir_path = np_maze[pos[0]][pos[1]:]
        if "#" not in dir_path:
            for i in range(pos[0], len(np_maze[0]), 1):
                visited.add(f"{pos[0]},{i}")
            break
        pos[1] += np.where(dir_path == "#")[0][0]-1
        dir = "down"
        for i in range(pos[1], pos[1]-np.where(dir_path == "#")[0][0], -1):
            visited.add(f"{pos[0]},{i}")
    elif dir == "down":
        dir_path = np_maze.T[pos[1]][pos[0]:]
        if "#" not in dir_path:
            for i in range(pos[0], len(np_maze), 1):
                visited.add(f"{i},{pos[1]}")
            break
        pos[0] += (np.where(dir_path == "#")[0][0]-1)
        dir = "left"
        for i in range(pos[0]-np.where(dir_path == "#")[0][0]+1, pos[0]+1):
            visited.add(f"{i},{pos[1]}")
    elif dir == "left":
        dir_path = np_maze[pos[0]][:pos[1]][::-1]
        if "#" not in dir_path:
            for i in range(pos[1], -1, -1):
                visited.add(f"{pos[0]},{i}")
            break
        pos[1] -= (np.where(dir_path == "#")[0][0])
        dir = "up"
        for i in range(pos[1], pos[1]+np.where(dir_path == "#")[0][0]+1):
            visited.add(f"{pos[0]},{i}")     

print(len(visited))

# Suppose loops can only be placed on guard's original path to have any effect
for obs in visited:
    pos = start_pos.copy()
    dir = "up"
    a, b = obs.split(",")
    np_maze[int(a)][int(b)] = "#"
    visited_dir = set()

    while(True):
        if dir == "up":
            dir_path = np_maze.T[pos[1]][:pos[0]][::-1]
            if "#" not in dir_path:
                break
            pos[0] -= np.where(dir_path == "#")[0][0]
            dir = "right"
        elif dir == "right":
            dir_path = np_maze[pos[0]][pos[1]:]
            if "#" not in dir_path:
                break
            pos[1] += np.where(dir_path == "#")[0][0]-1
            dir = "down"
        elif dir == "down":
            dir_path = np_maze.T[pos[1]][pos[0]:]
            if "#" not in dir_path:
                break
            pos[0] += (np.where(dir_path == "#")[0][0]-1)
            dir = "left"
        elif dir == "left":
            dir_path = np_maze[pos[0]][:pos[1]][::-1]
            if "#" not in dir_path:
                break
            pos[1] -= (np.where(dir_path == "#")[0][0])
            dir = "up"
        if (f"{pos[0]},{pos[1]},{dir}" in visited_dir):
            result+=1
            break
        visited_dir.add(f"{pos[0]},{pos[1]},{dir}")

    np_maze[int(a)][int(b)] = "."
   
print(result)