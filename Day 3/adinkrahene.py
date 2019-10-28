"""
Project Name: Learn Python in One Week
Developer Name: Truston Ailende
Email Address: truston@trustonailende.com
"""
# Import the turtle module
import turtle

# Write the code here
turtle.penup()
turtle.setposition(-200, 200)
turtle.pendown()
turtle.color("gold", "black")
turtle.pensize(5)

turtle.begin_fill()
turtle.forward(400)
turtle.right(90)
turtle.forward(400)
turtle.right(90)
turtle.forward(400)
turtle.right(90)
turtle.forward(400)
turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.home()
turtle.pensize(10)
turtle.setposition(0, -80)
turtle.pendown()
turtle.circle(80)

turtle.penup()
turtle.setposition(0, -130)
turtle.pendown()
turtle.circle(130)

turtle.penup()
turtle.setposition(0, -180)
turtle.pendown()
turtle.circle(180)
turtle.hideturtle()

# End the program loop
turtle.done()
