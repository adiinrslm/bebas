# casting adalah merubah tipe data satu ke tipe data yang lain

#integer
print("====INTEGER===")
data_int = 20
print("data = ", data_int, "type =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data = ", data_float, "type =", type(data_float))
print("data = ", data_str, "type =", type(data_str))
print("data = ", data_bool, "type =", type(data_bool))

#float
print("===FLOAT===")
data_float = 20.7
print("data = ", data_float, "type =", type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
print("data = ", data_int, "type =", type(data_int))
print("data = ", data_str, "type =", type(data_str))
print("data = ", data_bool, "type =", type(data_bool))

#string
print("===STRING===")
data_str = 0
print("data = ", data_str,"type =", type(data_str))

data_int = int(data_str) #STRING HARUS BERUPA ANGKA
data_float = float(data_str) 
data_bool = bool(data_str) #STRING AKAN FALSE JIKA KOSONG
print("data =", data_int, "type =", type(data_int))
print("data =", data_float, "type =", type(data_float))
print("data =", data_bool, "type =", type(data_bool))

#boolean
print("===BOOLEAN====")
data_bool = True
print("data =", data_bool, "type =", type(data_bool))

data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)
print("data =", data_int, "type =", type(data_int))
print("data =", data_float, "type =", type(data_float))
print("data =", data_str, "type =", type(data_str))