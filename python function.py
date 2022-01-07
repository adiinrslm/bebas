# first example
# To create a function, we use the def keyword followed by the function name, parenthesis (), and a colon :. The body of the function is specified using indentation.
def greet():
    print("Hello")
    print("How do you do?")
greet()


# function arguments
def greet(name):
    print("Hello", name)
    print("How do you do?")
greet("Jack")


# passing multiple arguments
def add_numbers(n1, n2):
    result = n1 + n2
    print("The sum is", result)

number1 = 5.4
number2 = 6.7
add_numbers(number1, number2)


# return value from function
def add_numbers(n1, n2):
    result = n1 + n2
    return result

result = add_numbers(5.4, 6.7)
print("The sum is", result)


# another example
marks = [55, 64, 75, 80, 65]
#You want to find the average marks you obtained in the exam.
#Based on the average marks you want to find your grade as:
#You will get Grade A if the average marks is equal to or above 80
#You will get Grade B if the average marks is equal to or above 60 and less than 80
#You will get Grade C if the average marks is equal to or above 50 and less than 60
#And if the average marks is less than 50, you will get Grade F
# find the average marks and return it
def find_average_marks(marks):
    sum_of_marks = sum(marks)
    number_of_subjects = len(marks)
    
    average_marks = sum_of_marks/number_of_subjects
    
    return average_marks

# compute grade and return it
def compute_grade(average_marks):
    if average_marks >= 80.0:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    
    return grade

marks = [55, 64, 75, 80, 65]
average_marks = find_average_marks(marks)
grade =compute_grade(average_marks)

print("Your average marks is", average_marks)
print("Your grade is", grade)


# last example
# create a program to add and multiply two numbers
# For this, create two functions add_numbers() and multiply_numbers(). 
# These functions should compute the result and return them to the function call 
# and should print from outside the function.
# function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# function to multiply two numbers
def multiply_numbers(num1, num2):
    return num1 * num2

number1 = 5
number2 = 30

sum_result = add_numbers(number1, number2)
print("Sum is", sum_result)

product_result = multiply_numbers(number1, number2)
print("Product is", product_result)