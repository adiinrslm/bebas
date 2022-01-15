# In Python, global keyword allows you to modify the variable outside of the current scope. 
# It is used to create a global variable and make changes to the variable in a local context.

#Rules of global Keyword
#The basic rules for global keyword in Python are:
#When we create a variable inside a function, it is local by default.
#When we define a variable outside of a function, it is global by default. You don't have to use global keyword.
#We use global keyword to read and write a global variable inside a function.
#Use of global keyword outside a function has no effect.

# Example 1: Accessing global Variable From Inside a Function
c = 1 # global variable

def add():
    print(c)

add()


# Example 2: Modifying Global Variable From Inside the Function
c = 1 # global variable
    
def add():
    c = c + 2 # increment c by 2
    print(c)

add()
# When we run the above program, the output shows an error
# This is because we can only access the global variable but cannot modify it from inside the function.
# The solution for this is to use the global keyword.

# Example 3: Changing Global Variable From Inside a Function using global
c = 0 # global variable

def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()
print("In main:", c)

# Global in Nested Functions
# Example 5: Using a Global Variable in Nested Function
def foo():
    x = 20

    def bar():
        global x
        x = 25
    
    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)

foo()
print("x in main: ", x)