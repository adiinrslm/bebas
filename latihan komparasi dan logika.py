# latihan komparasi dan logika dasar
# membuat area rentang dari angka

# ++++++3-------10+++++++

inputUser = float(input('masukan angka yang bernilai\nkurang dari 3\natau lebih besar dari 10\n:'))

# ++++++3--------------------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print('kurang dari 3 =',isKurangDari) 

# ------------10+++++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print('lebih dari 10 =',isLebihDari)

# ++++++3-------10+++++++
isCorrect = isKurangDari or isLebihDari
print('angka yang anda masukan :',isCorrect)


print('===============')
# -------3++++++10--------
# ini adalah kasus irisan
inputUser = float(input('masukan angka yang bernilai\nlebih dari 3\ndan kurang dari 10\n:'))

# ----3+++++++++
# lebih dari 3
isLebihDari = inputUser > 3
print('lebih dari 3 =',isLebihDari)

# +++++++++10-------------
# kurang dari 10
isKurangDari = inputUser < 10
print('kurang dari 10 =',isKurangDari)

isCorrect = isKurangDari and isLebihDari
print('angka yang anda masukan :',isCorrect)



# Cara lain
print('===============')
x = float(input('masukan angka :'))
if (x>0 and x<5) or (x>8 and x<11) :
    print(True)
else :
    print(False)

print('===============')
x = float(input('masukan angka :'))
if (x<0 and x>5) or (x<8 and x>11) :
    print(True)
else :
    print(False)