# python break statement

for item in range(2, 6):
    print(item)
    break

# using break statement with for
for item in range(1, 6):
    if item == 3:
        break
    print(item)

print("The end")

# using break with while
while True:
    number = float(input("Enter a number: "))
    if number < 0:
        break
    print("You entered:", number)

# python continue statement
for item in range(2, 6):
    print(item)
    continue

# using continue statement with for
for i in range(5):
    number = float(input("Enter a number: "))

    # check if number if negative
    if number < 0:
        continue

    print(number)

# another examples
#create a program that all items of the languages list are printed except Swift and C++
languages = ["Python", "Java", "Swift", "C", "C++"]

for language in languages:
    if language == "Swift" or language == "C++":
        continue
    print(language)