# Python List
# a list of integers
numbers = [1, 5, 6, -4]
print(numbers)

# mixed list
random_list = [2.5, "Hello", -5, 2.5]
print(random_list)

# empty list
list1 = []
print(list1)

# use the built-in len() function to find length of a list.
# a list of integers
numbers = [1, 5, 6, -4]
print(len(numbers))

# empty list
list1 = []
print(len(list1))

# Access List Elements
languages = ["Python", "JavaScript", "C++", "Kotlin"]
print(languages)


# Negative Indexing
# In Python, we can also use negative indexing for sequences like lists. Using a negative index gives us items from the last.

languages = ["Python", "JavaScript", "C++", "Kotlin"]

# last element
print(languages[-1])

# third to last element
print(languages[-3])


# Slicing of a List
languages = ["Python", "JavaScript", "C++", "Kotlin"]

# first three items -> 0, 1, 2
print(languages[0:3])

# second to last items -> 1, 2, 3
print(languages[1:4])

# Change Items of a List
languages = ["Python", "JavaScript", "C++", "Kotlin"]

# modifying the second item
languages[1] = "Ruby"

print(languages)

# in keyword
# The in keyword is used to check whether an item is in the list or not.
languages = ["Python", "JavaScript", "C++", "Kotlin"]
print("Python" in languages)

print("Rust" in languages)


# Iterating through a List
languages = ["Python", "JavaScript", "C++", "Kotlin"]

for language in languages:
    print(language)

# List Methods
languages = ["Python", "JavaScript", "C++", "Kotlin"]
languages.append("Rust")

print(languages)

# insert() method
languages = ["Python", "JavaScript", "C++", "Kotlin"]
languages.insert(1, "Rust")

print(languages)


# remove() method
languages = ["Python", "JavaScript", "C++", "Kotlin"]
languages.remove("C++")

print(languages)


# copy() method
languages = ["Python", "JavaScript", "C++", "Kotlin"]

languages1 = languages.copy()
print(languages1)


# Python Tuples
numbers = (21, -5, 6, 9)
print(numbers)
