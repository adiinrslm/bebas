# ini adalah operasi logika sederhana 
# not, or, and, xor

# NOT
print("====NOT====")
a = True
b = not a
print('data a =',a)
print('------------NOT')
print('data b =',b)

# OR (jika salah satu true, maka hasilnya true)
print("====OR====")
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)

a = False
b = True
c = a or b
print(a,'OR',b,'=',c)

a = True
b = False
c = a or b
print(a,'OR',b,'=',c)

a = True
b = True
c = a or b
print(a,'OR',b,'=',c)

# AND (jika salah satu true, maka hasilnya false)
# harus terdapat dua true jika ingin hasil akhirnya true
print("====AND====")
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)

a = False
b = True
c = a and b
print(a,'AND',b,'=',c)

a = True
b = False
c = a and b
print(a,'AND',b,'=',c)

a = True
b = True
c = a and b
print(a,'AND',b,'=',c)

# XOR (akan true jika salah satu true, sisanya false)
# tapi jika dua data true, hasilnya akan false
print("====XOR====")
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)

a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)