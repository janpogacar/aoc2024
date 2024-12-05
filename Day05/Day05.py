from functools import cmp_to_key

def compare(item1, item2):
    return -1 if [item1, item2] in page_rules else 1

input_file = open("input05_01.txt", "r")  
page_rules = input_file.read().split("\n")
for i, x in enumerate(page_rules):
    page_rules[i] = x.split("|")

input_file_2 = open("input05_02.txt", "r") 
updates = input_file_2.read().split("\n")
for i, x in enumerate(updates):
    updates[i] = x.split(",")

result_list = []
result_list_p2 = []
for i, x in enumerate(updates):
    sorted_x = sorted(x, key=cmp_to_key(compare))
    if sorted_x == x:
       result_list.append(x)
    else:
       result_list_p2.append(sorted_x)

result = 0
for x in result_list:
    result += int(x[int((len(x) - 1)/2)])

print(result)

result = 0
for x in result_list_p2:
    result += int(x[int((len(x) - 1)/2)])

print(result)