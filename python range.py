# using range()
result = range(1, 11)
print(result)

# The range() function returns a range object which is a sequence of numbers. 
# We can see what is inside this object by converting it to other types like list.
result = range(1, 11)

# converting to list
result = list(result)

print(result)

# range() in for Loop
for value in range(1, 6):
    print(value, "iteration")

# range() with only stop Parameter
result = range(11)

result = list(result)
print(result)


# range() with step Parameter
result = list(range(1, 11))
print(result)

# We can also use negative numbers in the range function
result = list(range(5, -6, -1))
print(result)

