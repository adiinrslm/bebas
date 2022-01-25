# create a string
# single quote
text = 'Hello there'
print(text)

# double quotes
text = "Hello there"
print(text)

# triple quotes for multiline strings
text = """Hello there.
How are you doing"""
print(text)

# access string character
text = "Python"
print(text)
# We can use indices in the following way:
text = "Python"

# first character
print(text[0])

# fourth character
print(text[3])

# negative indexing
text = "Python"
# last character
print(text[-1])
# third to last character
print(text[-3])


# slicing a string
text = "Python"
# 2nd, 3rd and 4th characters
print(text[1:4])


# change and delete character
text = "Python"
text[0] = "p"
print(text)

# python string operations
text1 = "Python"
text2 = "Programming"

result = text1 + " " + text2
print(result)


# iterating through a string
text = "Python"

for character in text:
    print(character) 


# python string methods
text = "I like Python 3"
result = text.lower()

print(result)


# find() methods
text = "I like Python 3"
result = text.find("Python")

print(result)


# replace() methods
text = "I like Python 3"
result = text.replace("Python 3", "Java")

print(result)