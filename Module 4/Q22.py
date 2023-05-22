# Write a pyhton  class nameed rectangle constucted by length and width and a method which will compute the area os rectangle  .
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Example usage:
rect = Rectangle(5, 10)
print(rect.area()) # Output: 50