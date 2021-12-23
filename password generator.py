<<<<<<< HEAD
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
    
=======
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
    
>>>>>>> 4c62db80eff798c1e681cd007c3e937836c93b6f
    print(passwords)