# create dictionaries
person1 = {"name": "Linus", "age": 21}
print(person1)

# access dictionary elements
person1 = {"name": "Linus", "age": 21}
print(person1["name"])
print(person1["age"])

# add and change dictionary elements
person1 = {"name": "Linus", "age": 21}

# changing existing keys
person1["name"] = "Dennis"
print(person1)

# adding new keys
person1["hobbies"] = ["dancing", "fishing"]
print(person1)

# remove elements from a dictionary
person1 = {"name": "Linus", "age": 21}
print(person1.pop("name"))

print(person1)


# iterating through a dictionary
person1 = {"name": "Linus", "age": 21}

for key in person1:
   print(key)
   print(person1[key])