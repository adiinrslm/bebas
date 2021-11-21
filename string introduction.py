from typing import OrderedDict


data = 'ini adalah string introduction'
print(data)
print(type(data))

# 1. membuat string
'''
    1. menggunakan single quote '...'
    2. menggunakan double quote "..."
'''

data = 'ini adalah penggunaan single quote'
print(data)

data = "ini adalah penggunaan double quote"
print(data)

# contoh lain
print('"Hi, how are you?"') # bisa dipakai dalam percakapan
print("'Hi, how are you?'")
print("ini adalah hari jum'at") # single quote disini terdeteksi sebagai string

# 2. menggunakan tanda \

# membuat tanda ' agar terdeteksi sebagai string
print('it\'s only me')
print('i\'m not an engineering')

# dengan backslash
print('c:\\user\\adinursalam')

# dengan tab -> hasil running akan berjauhan
print('muhamad\tadi\tnursalam')

# dengan backspace -> hasil running akan berdekatan
print('muhamad \badi \bnursalam')

# newline
print('baris pertama.\nbaris kedua.') # LF = Line Feed -> unix, MacOs, linux
print('baris pertama.\rbaris kedua.') # CR = Carriage Return -> commodore, acorn
print('baris pertama.\r\nbaris kedua.') # CRLF = Carriage Return Line Feed -> windows

# 3. menggunakan string literal atau raw string

# memakai raw string
print(r'c:\user\adinursalam') # 'r' disini adalah raw string nya

# multiline literal string
print("""
Nama : Muhamad Adi Nursalam
Kelas : XII IPS 5
""")

# multiline literal string dan RAW  
# dengan raw string, semua huruf, angka, simbol setelah 'r' akan -
# - terdeteksi sebagai string
print(r"""
Nama : Muhamad Adi Nursalam
Website : www.adiinrslm.com//newprofile
""")