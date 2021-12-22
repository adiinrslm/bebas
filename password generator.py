import random 

print("Welcome To Password Generator")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$?/'

number = input('Amount of passwords to generate: ')
number = int(number)

length = input("Input your passwords length: ")
length = int(length)

print('\nHere are your passwords: ')

for passwords in range (number):
    passwords = ''
    for c in range (length):
        passwords += random.choice(chars)
    
    print(passwords)