from collections import defaultdict
import matplotlib.pyplot as plt 

def array_to_complex_defaultdict(matrix):
    result = defaultdict(dict)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            complex_key = complex(col, row)
            result[complex_key]['value'] = matrix[row][col]
            result[complex_key]['nodes'] = []
    return result

def dfs(visited, graph, node):  #function for dfs 
    global result
    if (node not in visited):
        visited.add(node)
        for neighbour in graph[node]["nodes"]:
            dfs(visited, graph, neighbour)

input_file = open("input12.txt", "r")
maze = input_file.read().split("\n")

for i, x in enumerate(maze):
    maze[i] = list(x)

farm_dict = array_to_complex_defaultdict(maze) # index array to dict

for x in list(farm_dict.keys()): # Set up nodes for graph traversal
    for i,j in [[0,-1], [0,1], [-1,0], [1,0]]:
        if len(farm_dict[x+complex(i,j)]) != 0:
            if farm_dict[x+complex(i,j)]["value"] == farm_dict[x]["value"]:
                farm_dict[x]["nodes"].append(x+complex(i,j)) 

regions = defaultdict(set)

all_visited = set()

region_index = 0
for im in range(len(maze)):
    for re in range(len(maze[0])):
        if complex(im,re) not in all_visited:
            visited = set()
            dfs(visited, farm_dict, complex(im,re))
            regions[region_index] = visited
            region_index += 1
            all_visited.update(visited)

result = 0
result2 = 0
for region in regions:
    border = []
    corner = []
    for x in regions[region]:
        im = int(x.imag)
        re = int(x.real)
        for i,j in [[0,-1], [0,1], [-1,0], [1,0]]:
            if (complex(re+j, im+i) not in regions[region]):
                border.append(complex(im+i,re+j))
        # Find corners
        if (complex(re+0, im-1) not in regions[region]) and (complex(re+1, im+0) not in regions[region]) :
                corner.append(complex(re,im))
        if (complex(re+1, im-0) not in regions[region]) and (complex(re+0, im+1) not in regions[region]) :
                corner.append(complex(re,im))
        if (complex(re+0, im-1) not in regions[region]) and (complex(re-1, im+0) not in regions[region]) :
                corner.append(complex(re,im))
        if (complex(re-1, im-0) not in regions[region]) and (complex(re+0, im+1) not in regions[region]) :
                corner.append(complex(re,im))
        # Concave corners
        if (complex(re+1, im-1) not in regions[region]) and (complex(re+0, im-1) in regions[region]) and (complex(re+1, im-0) in regions[region]):
                corner.append(complex(re,im))
        if (complex(re-1, im-1) not in regions[region]) and (complex(re-0, im-1) in regions[region]) and (complex(re-1, im-0) in regions[region]):
                corner.append(complex(re,im))
        if (complex(re-1, im+1) not in regions[region]) and (complex(re+0, im+1) in regions[region]) and (complex(re-1, im-0) in regions[region]):
                corner.append(complex(re,im))
        if (complex(re+1, im+1) not in regions[region]) and (complex(re+0, im+1) in regions[region]) and (complex(re+1, im-0) in regions[region]):
                corner.append(complex(re,im))
            

   
    result += len(border)*len(regions[region])
    result2 += len(corner)*len(regions[region])

print(result)
print(result2)