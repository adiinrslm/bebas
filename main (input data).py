# data yang dimasukan pasti berupa string
data = input("masukan data : ")
print("data = ",data, ",type =", type(data))

# jika ingin mengambil data integer, maka
angka = float(input("masukan angka : "))
angka = int(input("masukan angka : "))
print("data =",data,",type =", type(angka))

# jika datanya boolean, maka
biner = bool(int(input("masukan nilai boolean : ")))
print("data = ",data,", type =", type(biner))