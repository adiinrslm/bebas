#   Create Lambda Functions
def double(n):
    return n * 2


print(double(10))

# or we can use this way
double = lambda n: n * 2

print(double(10))

# The syntax of lambda function is: (lambda arguments: expression)

larger = lambda a, b: a if a > b else b

print(larger(22, 21))


# lambda functions as keys to sort()
names = ['Alan', 'Gregory', 'Zlatan', 'Jonas', 'Tom', 'Augustine']

names.sort()
print(names)

# We can do this by passing an optional key argument to the sort() method.
names = ['Alan', 'Gregory', 'Zlatan', 'Jonas', 'Tom', 'Augustine']

names.sort(key=lambda x: len(x))
print(names)