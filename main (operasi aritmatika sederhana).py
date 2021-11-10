# operasi aritmatika
a = 21
b = 5

# pertambahan +
hasil = a + b
print(a,"+",b,"=",hasil)

# pengurangan -
hasil = a - b
print(a,"-",b,"=",hasil)

# perkalian *
hasil =a * b
print(a,"*",b,"=",hasil)

# pembagian / (otomatis menjadi data float/desimal)
hasil = a / b
print(a,"/",b,"=",hasil)

# eksponen (pangkat) **
hasil = a ** b
print(a,"**",b,"=",hasil)

# modulus (sisa pembagian) %
hasil = a % b
print(a,"%",b,"=",hasil)

# floor division //
hasil = a // b
print(a,"//",b,"=",hasil)

# prioritas operasi, operational precedence
# (), eksponen, perkalian/pembagian/modulus/floor division
# = , pertambahan/pengurangan

a = 3
b = 5
c = 21
hasil = a ** b // c + c - a % a * a
print(a ,"**",b,"//",c,"+",c ,"-",a,"%",a,"*",a,"=",hasil)

# tanda kurung akan mengambil langkah pertama
hasil = ( a * b) - c
print( "(",a,"*",b,")","-",c,"=",hasil)