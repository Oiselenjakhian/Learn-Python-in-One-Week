"""
Project Name: Learn Python in One Week
Developer Name: Truston Ailende
Email Address: truston@trustonailende.com
"""
# Define a function for the average of three numbers
def average_three(first_number, second_number, third_number):
    average = (first_number + second_number + third_number) / 3
    return round(average, 2)

# Ask the user for the first number
first_number = float(input("Please enter the first number: "))

# Ask the user for the second number
second_number = float(input("Please enter the second number: "))

# Ask the user for the third number
third_number = float(input("Please enter the third number: "))

# Calculate the average and display it
print(average_three(first_number, second_number, third_number))

