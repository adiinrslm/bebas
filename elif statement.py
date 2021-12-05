# ELIF = else if statement

print("==FIRST EXAMPLE==")
num = int(input("Enter your number: "))


if num > 0:
     print("positive number")
elif num == 0:
    print("Zero")
else:
    print("negative number")


print("\n==SECOND EXAMPLE==")
result = int(input("Enter your price: "))

if result > 100:
    print("price is greater than 100")
elif result == 100:
    print("price is 100")
else:
    print("price is less than 100")



print("\n==ELIF WITH MULTIPLE CONDITIONS==")
a = 7
b = 9
c = 3

if((a>b and a>c) and (a != b and a != c)):
	print(a, " is the largest")
elif((b>a and b>c) and (b != a and b != c)):
	print(b, " is the largest")
elif((c>a and c>b) and (c != a and c != b)):
	print(c, " is the largest")
else:
	print("entered numbers are equal")

# outpout = 9  is the largest