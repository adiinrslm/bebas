# example
print("==DATA TYPE==")
a = 5

print(type(a))

print(type(5.0))

c = 5 + 3j
print(c + 3)

print(isinstance(c, complex))

#Number System	    Prefix
# Binary	        '0b' or '0B'
# Octal	            '0o' or '0O'
# Hexadecimal	    '0x' or '0X'

# example of prefix
# Output: 107
print(0b1101011)

# Output: 253 (251 + 2)
print(0xFB + 0b10)

# Output: 13
print(0o15)

# Type Conversion
#>>> int(2.3)
    #2
#>>> int(-2.8)
    #-2
#>>> float(5)
    #5.0
#>>> complex('3+5j')
    #(3+5j)


print("==PYTHON DECIMAL==")
import decimal
print(0.1)
print(decimal.Decimal(0.1))

# example
from decimal import Decimal as D

print(D('1.1') + D('2.2'))

print(D('1.2') * D('2.50'))


# Python Fractions
print("==PYTHON FRACIONS==")
import fractions

print(fractions.Fraction(1.5))

print(fractions.Fraction(5))

print(fractions.Fraction(1,3))

# example again
from fractions import Fraction as F

print(F(1, 3) + F(1, 3))

print(1 / F(5, 6))

print(F(-3, 10) > 0)

print(F(-3, 10) < 0)

# PYTHON MATHEMATICS
print("==PYTHON MATHEMATICS==")
import math

print(math.pi)

print(math.cos(math.pi))

print(math.exp(10))

print(math.log10(1000))

print(math.sinh(1))

print(math.factorial(6))