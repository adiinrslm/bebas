# Operasi komparasi
# Data yang dihasilkan pasti berupa boolean ( true/false )
# >,<,>=,<=,==,!=,is,is not

a = 10
b = 5

# lebih besar dari >
print('=====lebih besar dari (>)')
hasil = a > 5
print(a,'>',5,'=',hasil)

hasil = b > 10
print(b,'>',10,'=',hasil)

hasil = b > 5
print(b,'>',5,'=',hasil)

# kurang dari <
print('=====kurang dari (<)')
hasil = a < 5
print(a,'<',5,'=',hasil)

hasil = b < 10
print(b,'<',10,'=',hasil)

hasil = b < 5
print(b,'<',5,'=',hasil)

# lebih dari sama dengan >=
print('=====lebih dari sama dengan (>=)')
hasil = a >= 5
print(a,'>=',5,'=',hasil)

hasil = b >= 10
print(b,'>=',10,'=',hasil)

hasil = b >= 5
print(b,'>=',5,'=',hasil)

# kurang dari sama dengan (<=)
print('=====kurang dari sama dengan (<=)')
hasil = a <= 5
print(a,'<=',5,'=',hasil)

hasil = b <= 10
print(b,'<=',10,'=',hasil)

hasil = b <= 5
print(b,'<=',5,'=',hasil)

# sama dengan ( == )
print('=====sama dengan (==)')
hasil = a == 5
print(a,'==',5,'=',hasil)

hasil = b == 10
print(b,'==',10,'=',hasil)

hasil = b == 5
print(b,'==',5,'=',hasil)

# tidak sama dengan ( != )
print('=====tidak sama dengan (!=)')
hasil = a != 5
print(a,'!=',5,'!=',hasil)

hasil = b != 10
print(b,'!=',10,'=',hasil)

hasil = b != 5
print(b,'!=',5,'=',hasil)

# 'is' sebagai komparasi identity object
# hanya untuk object dengan nilai yang serupa hasilnya akan true
# jika berbeda object, hasilnya false
print('=====object identity (is)')
x = 20 # ini adalah assignment membuat object
y = 20

print('nilai x =',x,',id = ',hex(id(x)))
print('nilai x =',y,',id = ',hex(id(y)))
hasil = x is 7
print('x is y =',hasil)

# 'is not' sebagai komparasi identity object
# untuk object dengan nilai berbeda hasilnya akan true
# jika berbeda object, hasilnya false
print('=====object identity (is not)')
x = 20 # ini adalah assignment membuat object
y = 9

print('nilai x =',x,',id = ',hex(id(x)))
print('nilai x =',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is not y =',hasil)
