from sys import argv

# Ex. "python ./main.py 12 3 2"
input1 = int(argv[1])  # 12
input2 = int(argv[2])  # 3
operation = int(argv[3])  # 2 (Mult)

if operation == 0:
    solution = input1 + input2
elif operation == 1:
    solution = input1 - input2
elif operation == 2:
    solution = input1 * input2
elif operation == 3 and input2 != 0:
    solution = input1 / input2
else:
    solution = "Error!"
print(solution)
