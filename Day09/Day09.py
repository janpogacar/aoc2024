import copy
def checkConsecutive(l):
    return sorted(l) == list(range(min(l), max(l)+1))

input_file = open(r"C:\Repos\aoc2024\Day09\input09.txt", "r")
seq = input_file.read()

diskmap = []
dot = False
num = 0
for i,x in enumerate(seq):
    for j in range(int(x)):
        if dot:
            diskmap.append(".")
        else:
            diskmap.append(num)
    
    dot = not(dot)
    if not(dot):
        num += 1

pointlist = []
dotlist = []
freespots = [] # [loc, size]
point_regs = [] # [loc, size, num]
for i, x in enumerate(diskmap):
    if type(x) is int:
        pointlist.append([i,x])
    else:
        dotlist.append(i)

prev = ""
i = 0
j = 1
start = 0
diskmap.append("x")
while(i < len(diskmap)-1):
    if diskmap[i+1] != diskmap[i]:
        if type(diskmap[i]) is int:
            point_regs.append([start, j, diskmap[i]])
            start = i+1
            j = 1
        else:
            freespots.append([start, j])
            start = i+1
            j = 1
    else:
        j+=1
    i+=1

for i in range(len(pointlist)):
    if pointlist[i][0] != i:
        pointlist.insert(i, pointlist.pop())
        pointlist[i][0] = i
    
result = 0

# part 1 result
for x in pointlist:
    result += (x[0]*x[1])

print(result)

# for part 2, loop over point_regs in reverse order
# Find the first fitting free spot
# if free spot exactly matches len of point reg, then remove it, else modify it
for i in range(len(point_regs)-1, -1, -1):
    for j in range(len(freespots)):
        if freespots[j][0] >= point_regs[i][0]:
            break 
        if freespots[j][1] == point_regs[i][1]:
            point_regs[i][0] = freespots[j][0]
            freespots.pop(j)
            break
        elif freespots[j][1] > point_regs[i][1]:
            freespots.append([point_regs[i][0], point_regs[i][1]])
            point_regs[i][0] = freespots[j][0]
            freespots[j][0] = freespots[j][0] + point_regs[i][1]
            freespots[j][1] = freespots[j][1] - point_regs[i][1]
            break
            
result = 0
for x in point_regs:
    for i in range(x[0], x[0]+x[1]):
        result += x[2]*i 

print(result)
    


print(0)