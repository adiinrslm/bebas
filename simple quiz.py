print('Let\'s play a game')
print('You choose a number and the program will tell you the color hiding on your number')
print('You should choose from 1 to 4')

a = int(input("Make your choose here: "))

if a == 1:
    print('BLUE')
elif a == 2:
    print('RED')
elif a == 3:
    print('GREEN')
elif a == 4:
    print('BLACK')
else:
    print('Error, you didn\'t choose any number')