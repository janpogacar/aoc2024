input_file = open("input03.txt", "r")  
data = input_file.read()

# Find all occurances of mul(
res = [i for i in range(len(data)) if data.startswith("mul(", i)]
do_s = [i for i in range(len(data)) if data.startswith("do(", i)]
dont_s = [i for i in range(len(data)) if data.startswith("don't(", i)]

result = 0
for i,x in enumerate(res):
    substring = data[x:]
    # Check if value preceding comma is an int, check if value between comma and ) is int
    if substring[4:(substring.find(","))].isnumeric() and substring[(substring.find(",")+1):(substring.find(")"))].isnumeric():
        result += int(substring[4:(substring.find(","))]) * int(substring[(substring.find(",")+1):(substring.find(")"))])

print(f"Part 1 result: {result}")

result = 0
mul_enabled = 1

for i,x in enumerate(data):
    if i in do_s:
        mul_enabled = 1
    elif i in dont_s:
        mul_enabled = 0
    elif (i in res) and mul_enabled:
        substring = data[i:]
        # Check if value preceding comma is an int, check if value between comma and ) is int
        if substring[4:(substring.find(","))].isnumeric() and substring[(substring.find(",")+1):(substring.find(")"))].isnumeric():
            result += int(substring[4:(substring.find(","))]) * int(substring[(substring.find(",")+1):(substring.find(")"))])

print(f"Part 2 result: {result}")