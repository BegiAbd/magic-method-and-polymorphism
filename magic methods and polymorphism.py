      "Magic methods"
class Lion():
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f'this is the object of the {self.name}'

    def __repr__(self):
        return "this desct for comp"

lion = Lion("Bob")

print(lion.name)

print(lion)

 "polymorphism"
class Square:
    def __init__(self,a):
        self.a = a

    def get_total(self):
        return self.a ** 2

    def __str__(self):
        return f"this is square"

class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def get_total(self):
        return self.a * self.b

    def __str__(self):
        return f"this is rect"

class Circle:
    def __init__(self,r):
        self.r = r

    def get_total(self):
        return 3.14 * self.r ** 2

    def __str__(self):
        return f"this is circle"

square = Square(5)
rect = Rectangle(3,5)
circle = Circle(5)

# print(square.get_total_of_square())
# print(rect.get_total_of_rectangle())
# print(circle.get_total_of_circle())

figures = [square,rect,circle]

# for figure in figures:
#     if isinstance(figure,Square):
#         print(figure.get_total_of_square())
#     elif isinstance(figure,Rectangle):
#         print(figure.get_total_of_rectangle())
#     elif isinstance(figure,Circle):
#         print(figure.get_total_of_circle())

for figure in figures:
    print(figure.get_total())
    print(figure)