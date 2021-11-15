# latihan konversi temperature
# ini adalah latihan perhitungan dasar sederhana

# program konversi satuan celcius ke satuan lainnya
print("==PROGRAM KONVERSI TEMPERATURE CELCIUS==")

celcius = float(input("masukan data celcius :"))
print("suhu adalah ",celcius, "Celcius")

# celcius ke reamur = rumusnya = 4/5 * celcius
reamur = (4/5)*celcius
print("suhu dalam reamur adalah ",reamur, "Reamur")

# celcius ke fahrenheit = rumusnya 9/5 * celcius + 32
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah ",fahrenheit, "Fahrenheit")

# celcius ke kelvin = rumusnya = celcius + 273
kelvin = celcius + 273
print("suhu dalam kelvin adalah ",kelvin, "Kelvin")

print("__________________________________________")
# program konversi satuan reamur ke satuan lainnya
print("==PROGRAM KONVERSI TEMPERATURE REAMUR==")

reamur = float(input("masukan data reamur :"))
print("suhu adalah",reamur,"Reamur")

# reamur ke celcius = rumusnya = 5/4 * reamur
celcius = 5/4 * reamur
print("suhu dalam celcius adalah",celcius,"Celcius")

# reamur ke fahrenheit = rumusnya = 9/4 * reamur + 32
fahrenheit = ((9/4) * reamur) + 32
print("suhu dalam fahrenheit adalah",fahrenheit,"Fahrenheit")

# reamur ke kelvin = rumusnya = 5/4 * reamur + 273
kelvin = ((5/4) * reamur) + 273
print("suhu dalam kelvin adalah",kelvin,"Kelvin")


print("__________________________________________")
# program konversi satuan fahrenheit ke satuan lainnya
print("==PROGRAM KONVERSI TEMPERATURE FAHRENHEIT==")

fahrenheit = float(input("masukan data fahrenheit :"))
print("suhu adalah ",fahrenheit,"Fahrenheit")

# fahrenheit ke celcius = rumusnya 5/9 * ( fahrenheit - 32)
celcius = 5/9 * (fahrenheit - 32)
print("suhu dalam celcius adalah",celcius, "Celcius")

# fahrenheit ke reamur = rumusnya 4/9 * ( fahrenheit - 32)
reamur = 4/9 * (fahrenheit - 32)
print("suhu dalam reamur adalah",reamur, "Reamur")

# fahrenheit ke kelvin = rumusnya (9/5 * (fahrenheit+32)) + 273
kelvin = (9/5 * (fahrenheit+32)) + 273
print("suhu dalam kelvin adalah",kelvin, "Kelvin")

print("__________________________________________")
# program konversi satuan kelvin ke satuan lainnya
kelvin = float(input("masukan data kelvin :"))
print("suhu adalah ",kelvin,"Kelvin")

# kelvin ke celcius = rumusnya (kelvin - 273)
celcius = kelvin - 273
print("suhu dalam kelvin adalah",celcius,"Celcius")

# kelvin ke reamur = rumusnya 4/5 * ( kelvin - 273)
reamur = 4/5 * ( kelvin - 273)
print("suhu dalam reamur adalah",reamur,"Reamur")

# kelvin ke Fahrenheit = rumusnya (5/9 * (kelvin-32)) - 273
fahrenheit = (5/9 * (kelvin-32)) - 273
print("suhu dalam fahrenheit adalah",fahrenheit,"Fahrenheit")