"""
Project Name: Learn Python in One Week
Developer Name: Truston Ailende
Email Address: truston@trustonailende.com
"""
import math
print("This is a program to find the area of a circle")
radius = float(input("Enter the radius: "))
area = radius * radius * math.pi
area = round(area, 2)
print(area)
