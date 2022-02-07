# exceptions
# write a program that will give us an error
numerator = 10
denominator = 0

print(numerator/denominator)
# Even though our code was correct syntax wise, it's not allowed to divide a number by 0 in Python. 
# This is an exception. In this case, we are getting the ZeroDivisionError exception.

# handling exceptions
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator/denominator

    print(result)
except:
    print("Denominator cannot be 0. Try again.")

print("Program ends")


# handling specific exceptions
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator/denominator

    print(result)
except ZeroDivisionError:
    print("Denominator cannot be 0. Try again.")

print("Program ends")


# another way to handling specific exceptions
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator/denominator

    print(result)
    
    my_list = [1, 2, 3]
    i = int(input("Enter index: "))
    print(my_list[i])
except ZeroDivisionError:
    print("Denominator cannot be 0. Try again.")
except IndexError:
    print("Index is wrong.")

print("Program ends")



# try...finally statement
try:
    print(1/0)
except:
    print("Wrong denominator")
finally:
    print("Always printed")