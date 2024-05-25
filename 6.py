class Shape:
    def __init__(self, width, length):
        self.width = width
        self.length = length

class Rectangle(Shape):
    def get_area(self):
        return self.width * self.length

    def get_perimeter(self):
        return 2 * (self.width + self.length)

class Square(Shape):
    def get_area(self):
        return self.width * self.width

    def get_perimeter(self):
        return 4 * self.width

rectangle = Rectangle(5, 10)
print(rectangle.get_area())                     
print(rectangle.get_perimeter())                 

square = Square(4, 4)
print(square.get_area())                  
print(square.get_perimeter())               
