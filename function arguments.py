# Default Arguments
def add_numbers(n1 = 100, n2 = 1000):
    result = n1 + n2
    return result

result = add_numbers(5.4)
print(result)


# Keyword Arguments
def greet(name, message):
    print("Hello", name)
    print(message)

greet("Jack", "What's going on?")

greet(message = "Howdy?", name = "Jill")