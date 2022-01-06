# the syntax of while loop
# while test_condition:
#   statement(s)

# example 
count = 0

while count < 5:
    print("I am inside a loop.")
    print("Looping is interesting.")

# example where programs that terminate at one point
# For that, we can alter the value of count at every iteration like:
count = 0

while count < 5:
    print("I am inside a Loop.")
    print("Looping is interesting.")
    count = count + 1

# To understand what is going on let's print the value of count:
#  count = 0
#while count < 5:
 #   print(count)
  #  count = count + 1
# the output  = 0, 1, 2, 3, 4
# the block of code executes only 5 times as count goes from 0 to 4. At count = 5 the test condition is False and the loop terminates.


# another example
count = 5

while count <= 10:
    print(count)
    count = count + 1

# multiplication table example
number = int(input("Enter a number: "))

count = 1

while count <= 10:
    product = number * count
    print(number, "x", count, "=", product)
    count = count + 1