# Write A python program to calculate surface volume and area of cylinder ?radius = float(input("Enter the radius of the cylinder: "))
from math import pi

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# Calculate the surface area of the cylinder
sa = 2 * pi * radius * height + 2 * pi * radius ** 2
print("The surface area of the cylinder is: ", round(sa, 2))

# Calculate the volume of the cylinder
vol = pi * radius ** 2 * height
print("The volume of the cylinder is: ", round(vol, 2))
