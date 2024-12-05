input_file = open("input05_01.txt", "r")  
page_rules = input_file.read().split("\n")
for i, x in enumerate(page_rules):
    page_rules[i] = x.split("|")

input_file_2 = open("input05_02.txt", "r") 
updates = input_file_2.read().split("\n")
for i, x in enumerate(updates):
    updates[i] = x.split(",")

result_list = []
for i, x in enumerate(updates):
    update_match = True
    for j in range(len(x)-1):
        if [x[j], x[j+1]] not in page_rules:
            update_match = False
            break
    if update_match == True:
        result_list.append(x)

result = 0
for x in result_list:
    result += int(x[int((len(x) - 1)/2)])


print(result)

result_list = []
for i, x in enumerate(updates):
    update_match = True
    sorted = False
    while(sorted == False):
        sorted = True
        for j in range(len(updates[i])-1):
            if [updates[i][j], updates[i][j+1]] not in page_rules:
                sorted = False
                update_match = False
                tmp = updates[i][j]
                updates[i][j] = updates[i][j+1]
                updates[i][j+1] = tmp
    if update_match == False:
        result_list.append(updates[i])

result = 0
for x in result_list:
    result += int(x[int((len(x) - 1)/2)])

print(result)