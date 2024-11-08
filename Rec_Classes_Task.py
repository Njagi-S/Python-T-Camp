# Define a class Rectangle with attributes width and height.
# Add methods area and perimeter to calculate the area and perimeter of the rectangle.
# Instantiate a few rectangle objects and print their area and perimeter.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
rec1 = Rectangle(46,90)
rec2 = Rectangle(60,20)
rec3 = Rectangle(80,35)
print(f"The area of the first rectangle is {rec1.area()} while the perimeter is {rec1.perimeter()}")
print(f"The area of the second rectangle is {rec2.area()} while the perimeter is {rec2.perimeter()}")
print(f"The area of the third rectangle is {rec3.area()} while the perimeter is {rec3.perimeter()}")