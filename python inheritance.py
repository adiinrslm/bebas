# inheritance in python
class Animal:
    def eat():
        print("I can eat")
        
class Dog(Animal):
    def bark(self):
        print("I can bark")

class Cat(Animal):
    def get_grumpy(self):
        print("I am getting grumpy.")

dog1 = Dog()

dog1.bark()
dog1.eat()

cat1 = Cat()
cat1.eat()

# another example
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines")

    def get_perimeter(self):
        value = 0
        for side in self.sides:
            value += side
        return value


class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges")


class Quadrilateral(Polygon):
    def display_info(self):
        print("A quadrilateral is a polygon with 4 edges")

t1 = Triangle([5, 6, 7])
perimeter = t1.get_perimeter()
print("Perimeter:", perimeter)


# method overriding
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter


class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges")
        Polygon.display_info(self)


class Quadrilateral(Polygon):
    def display_info(self):
        print("A quadrilateral is a polygon with 4 edges")

t1 = Triangle([5, 6, 7])
perimeter = t1.get_perimeter()
print("Perimeter:", perimeter)

t1.display_info()



# the super function()
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines")

    def get_perimeter(self):
        value = 0
        for side in self.sides:
            value += side
        return value


class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges")
        # Polygon.display_info(self)
        super().display_info()

class Quadrilateral(Polygon):
    def display_info(self):
        print("A quadrilateral is a polygon with 4 edges")

t1 = Triangle([5, 6, 7])
perimeter = t1.get_perimeter()
print("Perimeter:", perimeter)

t1.display_info()