# Write a pyhton  class nameed circle constucted by radius and two  method which will compute the area and the perimeter of a circel ?


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius



# create a new circle with radius 5
my_circle = Circle(5)

# compute the area and perimeter of the circle
area = my_circle.area()
perimeter = my_circle.perimeter()

# print the results
print(f"The area of the circle is {area:.2f}")
print(f"The perimeter of the circle is {perimeter:.2f}")


# area of the circle is 78.50
# The perimeter of the circle is 31.40
# # ``
