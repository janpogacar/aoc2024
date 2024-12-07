from itertools import product

input_file = open("input07.txt", "r")  
cals = input_file.read().split("\n")

ops = ["+", "*", "|"]
op_list = ["".join(i) for i in product(ops, repeat=3)]

result = 0
for nres, cal in enumerate(cals):
    res, nums = cal.split(": ")
    res = int(res)
    num_list = nums.split()
    op_list = ["".join(i) for i in product(ops, repeat=(len(num_list)-1))]
    for x in op_list:
        op_string = num_list[0]
        for i, y in enumerate(x):
            if y == "|":
                op_string += num_list[i+1]
            else:    
                op_string = op_string + y + num_list[i+1]
            op_string = str(eval(op_string))
            if int(op_string) > res:
                break
        if int(op_string) == res:
            result += res
            break
    #if int(op_string) > res:
    #    break
    print(nres)


print(0)