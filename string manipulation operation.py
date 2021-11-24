# string manipulation operation

# 1. menyambung string (concatenate)
first_name = "Muhamad"
middle_name = "Adi"
last_name = "Nursalam"

full_name = first_name + " " + middle_name + " " + last_name 
print(full_name)

# 2. menghitung panjang string
length = len(full_name)
print(length)

# 3. operator untuk string 
# ini dipakai untuk mengecek apakah ada komponen char atau string dalam string
x = "i"
status = x in full_name
print("string " + x + " ada di " + full_name +" "+ str(status))

x = "i"
status = x not in full_name
print("string " + x + " tidak ada di " + full_name +" "+ str(status))

# mengulang string
print("haha"*6)
print(6*"hehe") 

# indexing
print("index ke-0 : " + full_name[0]) # 0 disini adalah huruf awal
print("index ke-6 : " + full_name[6])
print("index ke-(-1) : " + full_name[-1]) # jika (-) maka akan diambil huruf awal dari belakang
print("index ke-[0:3] : " + full_name[0:4]) # jika seperti ini, maka angka belakang harus ditambah nilainya satu
print("index ke-[0,2,4,6,8,10] : " + full_name[0:10:2]) # 10 disini adalah jarak jedanya, dan 2 disini adalah kelipatannya

# smallest item
print("smallest item is: " + min(full_name)) # the result must be space
# biggest item
print("biggest item is: " + max(full_name))

ascii_code = ord(" ")
print("ASCII code for space is :" +str(ascii_code))
data = 117
print("char for ASCII 118 is : " + chr(data))

# 4. operator dalam bentuk method
data = "beli ikan bandeng di bandung"
jumlah = data.count("n")
print("jumlah n pada " + data + " = " + str(jumlah))

## merubah case dari string

# merubah ke upper case
example = "muhamad adi nursalam"
print("normal = " + example)
example = example.upper()
print("upper = " + example)

# merubah ke lower case
example = "PadjAjarAN UNiVersItY"
print("normal = " + example)
example = example.lower()
print("lower = " + example)

## pengecekan dengan isX methods
# lower case example
good = "night"
is_it_lower = good.islower()# the result must be boolean
print(good + " is lower = " + str(is_it_lower)) # we should doing casting to str

# upper case example
is_it_upper = good.isupper()# the result must be boolean
print(good + " is upper = " + str(is_it_upper)) # we should doing casting to str

# another isX methods
# isalpha() ---> for all alphabet
# isalnum() ---> for alphabet and number
# isdecimal() ---> for all numbers
# isspace() ---> for space, tab, newline (\n)
# istittle() ---> for word that start with upper case

tittle = "Free Guy"
is_it_tittle = tittle.istitle()
print(tittle + " is tittle = " + str(is_it_tittle))

# component check startswith() ----- endswith()
start_check = "Move Up".startswith("Move")
print("start is = " + str(start_check))

end_check = "Move Up".endswith("Up")
print("end is = " + str(end_check))

## penggabungan komponen join() ----- split()
pisah = ['iron', 'man']
merge = ' '.join(pisah)
print(merge)

merge = 'tony'.join(pisah)
print(merge)

merge = 'irontonyman'
print(merge.split('tony'))

# alokasi karakter rjust(), ljust(), center()
right = "right".rjust(10)
print("'"+right+"'")

left = "left".ljust(10)
print("'"+left+"'")

center = "center".center(30,"=")
print("'"+center+"'")

# kebalikannya ---> strip()
center = "center".strip("=") # menghilangkan tanda =
print("'"+center+"'")