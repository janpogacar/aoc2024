from collections import defaultdict

def array_to_complex_defaultdict(matrix):
    result = defaultdict(dict)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            complex_key = complex(col, row)
            result[complex_key]['value'] = matrix[row][col]
            result[complex_key]['nodes'] = []
            if matrix[row][col] == '0':
                start_locs.append(complex_key)
    return result

def dfs(visited, graph, node):  #function for dfs 
    global result
    if (node not in visited) or part2: # for part 2, just ignore previously visited nodes
        if graph[node]["value"] == '9':
            result += 1
        visited.add(node)
        for neighbour in graph[node]["nodes"]:
            dfs(visited, graph, neighbour)

input_file = open(r"input10.txt", "r")
maze = input_file.read().split("\n")

for i, x in enumerate(maze):
    maze[i] = list(x)

start_locs = []
maze_dict = array_to_complex_defaultdict(maze) # index array to dict

for x in list(maze_dict.keys()): # Set up nodes for graph traversal
    for i,j in [[0,-1], [0,1], [-1,0], [1,0]]:
        if len(maze_dict[x+complex(i,j)]) != 0 and maze_dict[x+complex(i,j)]["value"].isnumeric() and maze_dict[x]["value"].isnumeric(): 
            if int(maze_dict[x+complex(i,j)]["value"]) == (int(maze_dict[x]["value"])+1):
                maze_dict[x]["nodes"].append(x+complex(i,j)) 
part2 = False
result = 0
for start_loc in start_locs:
    visited = set()
    dfs(visited, maze_dict, start_loc)

print(result)

part2 = True
result = 0
for start_loc in start_locs:
    dfs(visited, maze_dict, start_loc)

print(result)
