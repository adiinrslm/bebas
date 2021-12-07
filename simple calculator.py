# simple calculcator for simple math problem solving

num_1 = int(input("Input your first number : ")) # if you want decimal num, use "float" instead of "int"
operator = input("operator (+,-,x,/) : ")
num_2 = int(input("Input your second number : "))

# the branch

if operator == "+":
    result = num_1 + num_2
    print(f"the result is: {result}")
elif operator == "-":
    result = num_1 - num_2
    print(f"the result is: {result}")
elif operator == "x" or operator == "*":
    result = num_1 * num_2
    print(f"the result is: {result}")
elif operator == "/":
    result = num_1 / num_2
    print(f"the result is: {result}")
else:
    print("Error")

