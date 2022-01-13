# local variables
# A variable declared inside the function's body or in the local scope is known as a local variable.

def add_numbers(n1, n2):
    result = n1 + n2
    return result

output = add_numbers(2, 5)
print(output)


# global variables
# In Python, a variable declared outside of the function or in global scope is known as a global variable.
# This means that a global variable can be accessed inside or outside of the function.

message = "How you doing?"

def greet():
    message = "How are you?"
    print("Message inside function:", message)

greet()
print("Message outside function:", message)

# The global variable tells Python that the variable we are referring to is the global variable.
# After we change the global message variable, the changes are reflected in the global scope as well.
