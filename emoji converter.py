message = input(">")
words = message.split(" ")
emojis = {
    ":)" : "😊",
    ":(" : "☹️",
    ":*" : "😘" # you can add another emojis there
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)