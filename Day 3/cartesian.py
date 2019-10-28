"""
Project Name: Learn Python in One Week
Developer Name: Truston Ailende
Email Address: truston@trustonailende.com
"""
import turtle
import math

# Square
def drawSquare(length):
    turtle.penup()
    turtle.setposition(-length/2.0, length/2.0)
    turtle.pendown()
    for i in range(0, 4):
        turtle.forward(length)
        turtle.right(90)
    turtle.penup()
    turtle.home()

# Horizontal lines
def drawHorizontalLine(length, division):
    pixelSpace = int(length / division)
    half = int(length / 2)
    for j in range((-half + pixelSpace), half, pixelSpace):
        turtle.penup()
        turtle.setposition(-half, j)
        turtle.pendown()
        turtle.forward(length)
    turtle.penup()
    turtle.home()

# Vertical lines
def drawVerticalLine(length, division):
    pixelSpace = int(length / division)
    half = int(length / 2)
    turtle.right(90)
    for k in range((-half + pixelSpace), half, pixelSpace):
        turtle.penup()
        turtle.setposition(k, half)
        turtle.pendown()
        turtle.forward(length)
    turtle.penup()
    turtle.home()

# Draw the grid
turtle.speed(1000000)
drawSquare(400)
drawHorizontalLine(400, 40)
drawVerticalLine(400, 40)

# Change the colour mode
turtle.colormode(255)

# Change the pencolor to red
turtle.pencolor(255, 0, 0)

# Draw the horizontal centre line
turtle.setposition(-200, 0)
turtle.pendown()
turtle.forward(400)
turtle.penup()

# Draw the vertical centre line
turtle.setposition(0, 200)
turtle.setheading(270)
turtle.pendown()
turtle.forward(400)

# Reset all the properties
turtle.home()
turtle.pencolor(0, 0, 0)

# Place code here
turtle.pensize(5)

turtle.color("red", "red")

def drawCircle(xPos, yPos):
    turtle.penup()
    turtle.setposition(xPos + 5, yPos)
    turtle.setheading(90)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()

drawCircle(-110, 60)
drawCircle(0, 110)
drawCircle(110, 60)
drawCircle(110, -110)
drawCircle(30, -110)
drawCircle(30, 0)
drawCircle(-30, 0)
drawCircle(-30, -110)
drawCircle(-110, -110)

def coordinateDistance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    D = math.sqrt((dx * dx) + (dy * dy))
    return D

def angleBetween(xStart, yStart, xEnd, yEnd):
    myradians = math.atan2(yEnd - yStart, xEnd - xStart)
    upperAngle = math.degrees(myradians)
    return upperAngle

def drawLine(xStart, yStart, xEnd, yEnd):
    distance = coordinateDistance(xStart, yStart, xEnd, yEnd)
    angle = angleBetween(xStart, yStart, xEnd, yEnd)
    turtle.penup()
    turtle.setposition(xStart, yStart)
    turtle.pendown()
    turtle.setheading(angle)
    turtle.forward(distance)

# Change the pencolour to black
turtle.pencolor(0, 0, 0)

drawLine(-110, 60, 0, 110)
drawLine(0, 110, 110, 60)
drawLine(110, 60, 110, -110)
drawLine(110, -110, 30, -110)
drawLine(30, -110, 30, 0)
drawLine(30, 0, -30, 0)
drawLine(-30, 0, -30, -110)
drawLine(-30, -110, -110, -110)
drawLine(-110, -110, -110, 60)
drawLine(-110, 60, 110, 60)
drawLine(110, -110, -30, -110)

# Hide the turtle
turtle.hideturtle()
