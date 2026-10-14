"""Instance methods: Rectangle area and perimeter
Problem: create a Rectangle class with length and breadth.
          Use instance methods to calculate its area and perimeter.
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect1 = Rectangle(10, 5)

print("Rectangle Area :", rect1.area())
print("Rectangle Perimeter :", rect1.perimeter())
