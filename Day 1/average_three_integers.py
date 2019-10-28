"""
Project Name: Learn Python in One Week
Developer Name: Truston Ailende
Email Address: truston@trustonailende.com
"""
print("This is a program to find the average of three numbers")
first_number = int(input("Please enter the first number: "))
second_number = int(input("Please enter the second number: "))
third_number = int(input("Please enter the third number: "))
running_total = first_number + second_number + third_number
average = running_total / 3
average = round(average, 2)
print("The average is", average)
