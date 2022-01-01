# Python sequences
text = "Python"
languages = ['English', 'French', 'German']

# using for loops
# 1
text = "Python"

for character in text:
    print(character)

# 2
languages = ["English", "French", "German"]

for language in languages:
    print(language)


# python range
for count in range(1, 6): # it used 6 instead 5, bcs last number doesn't include
    print(count)

# example loop with an input from users
number = int(input("Enter an integer: "))

for count in range(1, 11):
    product = number * count
    print(number, "*", count, "=", product)