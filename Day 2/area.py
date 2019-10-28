"""
Project Name: Learn Python in One Week
Developer Name: Truston Ailende
Email Address: truston@trustonailende.com
"""
import math

# Explain the purpose of the program
print("This program is an Area Calculator")

# Display the shapes menu
menu = int(input("What shape do you want to find the area of?" +
                 "\n1. Triangle" +
                 "\n2. Square" +
                 "\n3. Circle" +
                 "\nPlease choose a shape: "))

# Find the area of the shape chosen by the user
if (menu == 1):
    print("Area of a Triangle")
    breadth = float(input("Enter the breadth of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = breadth * height / 2
    print("The area of the triangle is", area)
elif(menu == 2):
    print("Area of a Square")
    length = int(input("Enter the length of the square: "))
    area = length * length
    print("The area of the square is", area)
elif(menu == 3):
    print("Area of a Circle")
    radius = float(input("Enter the radius of the circle: "))
    area = radius * radius * math.pi
    print("The area of the circle is: ", round(area, 2))
else:
    print("Invalid Selection")
