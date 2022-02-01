# Python Object-Oriented Programming

# Python Classes and Objects
class Student:
    pass

student1 = Student()
student2 = Student()

# we can start adding different attributes to these object instances.
class Student:
    pass

student1 = Student()
student1.name = "Harry"
student1.marks = 85

print(student1.name)
print(student1.marks)

# we can define methods inside a class.
class Student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False

student1 = Student()
student1.name = "Harry"
student1.marks = 85

did_pass = student1.check_pass_fail()
print(did_pass)


# The __init__() Method
class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False

student1 = Student("Harry", 85)
print(student1.name)
print(student1.marks)

# check if they passed or failed the exams using the check_pass_fail() method.
class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False

student1 = Student("Harry", 85)
did_pass = student1.check_pass_fail()
print(did_pass)

student2 = Student("Janet", 30)
did_pass = student2.check_pass_fail()
print(did_pass)


# Example: Add Two Complex Numbers
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def add(self, number):
        real = self.real + number.real
        imag = self.imag + number.imag
        result = Complex(real, imag)
        return result

n1 = Complex(5, 6)
n2 = Complex(-4, 2)
result = n1.add(n2)

print("real =", result.real)
print("imag =", result.imag)