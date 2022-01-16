# example modules
import math

number = 25
result = math.sqrt(number)
print(result)

print(math.pi)

# Python from...import statement
from math import pi, sin, sqrt

value = sin(pi/2)
print(value)

num = sqrt(64)
print(num)

# We can also use the from...import statement to import all definitions from a module using *:
from math import *

value = sin(pi/2)
print(value)

num = sqrt(64)
print(num)

# The dir() function
import math

print(dir(math))

