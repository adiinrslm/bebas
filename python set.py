# creating set
animals = {"dog", "cat", "tiger", "elephant"}
print(animals)

# add items to a set
animals = {"dog", "cat", "tiger", "elephant", "dog"}
animals.add("monkey")

print(animals)

# we can also pass multiple iterables to the update() method:
animals = {"dog", "tiger", "elephant"}
wild_animals = ["tiger", "leopard", "elephant"]

animals.update(wild_animals, {"dolphin"})
print(animals)


# remove items from a set
animals = {"tiger", "cat", "elephant", "dog"}
animals.remove("ferret")

print(animals)

# we can also remove all items in a set at once by using the clear() method.
animals = {"tiger", "cat", "elephant", "dog"}
animals.clear()

print(animals)

# check if an item is in a set
animals = {"tiger", "cat", "elephant", "dog"}
print("tiger" in animals)

print("ferret" in animals)

# iterating through a set
animals = {"tiger", "cat", "elephant", "dog"}

for animal in animals:
    print(animal)

# python set operations
domestic_animals = {"dog", "cat", "elephant"}
wild_animals = {"lion", "tiger", "elephant"}

animals = domestic_animals.union(wild_animals)
animals1 = animals = domestic_animals | wild_animals

print(animals)
print(animals1)

# intersection of two sets
domestic_animals = {"dog", "cat", "elephant"}
wild_animals = {"lion", "tiger", "elephant"}

animals = domestic_animals.union(wild_animals)
animals1 = animals = domestic_animals | wild_animals

print(animals)
print(animals1)