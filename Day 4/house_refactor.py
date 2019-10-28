"""
Project Name: Learn Python in One Week
Developer Name: Truston Ailende
Email Address: truston@trustonailende.com
"""
# Import the turtle module
import turtle
import math

# Write the code here
turtle.penup()
turtle.setposition(-110, 60)
turtle.pendown()
turtle.pensize(5)

# Find the distance between the coordinates
def coordinate_distance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    D = math.sqrt((dx * dx) + (dy * dy))
    return D

# Find the angle between the coordinates
def angle_between(x_start, y_start, x_end, y_end):
    my_radians = math.atan2(y_end - y_start, x_end - x_start)
    upper_angle = math.degrees(my_radians)
    return upper_angle

def draw_line(x_start, y_start, x_end, y_end):
    distance = coordinate_distance(x_start, y_start, x_end, y_end)
    angle = angle_between(x_start, y_start, x_end, y_end)
    turtle.penup()
    turtle.setposition(x_start, y_start)
    turtle.pendown()
    turtle.setheading(angle)
    turtle.forward(distance)

draw_line(-110, 60, 0, 110)
draw_line(0, 110, 110, 60)
draw_line(110, 60, 110, -110)
draw_line(110, -110, 30, -110)
draw_line(30, -110, 30, 0)
draw_line(30, 0, -30, 0)
draw_line(-30, 0, -30, -110)
draw_line(-30, -110, -110, -110)
draw_line(-110, -110, -110, 60)
draw_line(-110, 60, 110, 60)
draw_line(30, -110, -30, -110)

# Hide the turtle
turtle.hideturtle()
