# width and multiline

# data
name_data = "her"
age_data = 18
height_data = 160
shoe_number_data = 39

# standard string
print(5*"="+"STANDARD STRING"+"="*5)
string_data = f"name = {name_data}, age = {age_data}, height = {height_data}, shoes = {shoe_number_data}"
print(string_data)

# string with multiline (\n)
print("\n"+5*"="+"MULTILINE STRING"+"="*5)
string_data = f"name = {name_data}, \nage = {age_data}, \nheight = {height_data}, \nshoes = {shoe_number_data}"
print(string_data)

# string multiline (triple quotes)
print("\n"+5*"="+"MULTILINE STRING"+"="*5)
string_data = f""""
name = {name_data}
age = {age_data}
height = {height_data}
shoe = {shoe_number_data}
"""
string_data = f"name = {name_data}, \nage = {age_data}, \nheight = {height_data}, \nshoes = {shoe_number_data}"
print(string_data)

# set width
print("\n"+5*"="+"SET WIDTH STRING"+"="*5)

data_string = f"""
name   = {name_data:>5}
age    = {age_data:>5}
height = {height_data:>5}
shoes  = {shoe_number_data:>5}
"""
print(data_string)