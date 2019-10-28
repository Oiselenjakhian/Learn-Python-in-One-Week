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

myradians = math.atan2(110 - 60, 0 - (-110))
angle1 = math.degrees(myradians)

dx = -110 - 0
dy = 60 - 110
distance1 = math.sqrt((dx * dx) + (dy * dy))

turtle.setheading(angle1)
turtle.forward(distance1)

myradians = math.atan2(60 - 110, 110 - 0)
angle2 = math.degrees(myradians)

dx = 0 - 110
dy = 110 - 60
distance2 = math.sqrt((dx * dx) + (dy * dy))

turtle.setheading(angle2)
turtle.forward(distance2)

myradians = math.atan2(-110 - 60, 110 - 110)
angle3 = math.degrees(myradians)

dx = 110 - 110
dy = 60 - (-110)
distance3 = math.sqrt((dx * dx) + (dy * dy))

turtle.setheading(angle3)
turtle.forward(distance3)

myradians = math.atan2(-110 - (-110), 30 - 110)
angle4 = math.degrees(myradians)

dx = 110 - 30
dy = -110 - (-110)
distance4 = math.sqrt((dx * dx) + (dy * dy))

turtle.setheading(angle4)
turtle.forward(distance4)

myradians = math.atan2(0 - (-110), 30 - 30)
angle5 = math.degrees(myradians)

dx = -110 - 0
dy = 30 - 30
distance5 = math.sqrt((dx * dx) + (dy * dy))

turtle.setheading(angle5)
turtle.forward(distance5)

myradians = math.atan2(0 - 0, -30 - 30)
angle6 = math.degrees(myradians)

dx = 30 -(-30)
dy = 0 - 0
distance6 = math.sqrt((dx * dx) + (dy * dy))

turtle.setheading(angle6)
turtle.forward(distance6)

myradians = math.atan2(-110 - 0, -30 - (-30))
angle7 = math.degrees(myradians)

dx = -30 - (-30)
dy = 0 - (-110)
distance7 = math.sqrt((dx * dx) + (dy * dy))

turtle.setheading(angle7)
turtle.forward(distance7)

myradians = math.atan2(-110 - (-110), -110 - (-30))
angle8 = math.degrees(myradians)

dx = -30 - (-110)
dy = -110 - (-110)
distance8 = math.sqrt((dx * dx) + (dy * dy))

turtle.setheading(angle8)
turtle.forward(distance8)

myradians = math.atan2(60 - (-110), -110 - (-110))
angle9 = math.degrees(myradians)

dx = -110 - (-110)
dy = -110 - 60
distance9 = math.sqrt((dx * dx) + (dy * dy))

turtle.setheading(angle9)
turtle.forward(distance9)

myradians = math.atan2(60 - 60, 110 - (-110))
angle10 = math.degrees(myradians)

dx = -110 - 110
dy = 60 - 60
distance10 = math.sqrt((dx * dx) + (dy * dy))

turtle.setheading(angle10)
turtle.forward(distance10)

turtle.penup()
turtle.setposition(30, -110)
turtle.pendown()

myradians = math.atan2(-110 - (-110), -30 - 30)
angle11 = math.degrees(myradians)

dx = 30 - (-30)
dy = -110 - (-110)
distance11 = math.sqrt((dx * dx) + (dy * dy))

turtle.setheading(angle11)
turtle.forward(distance11)

turtle.hideturtle()
