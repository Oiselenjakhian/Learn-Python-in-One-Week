"""
Project Name: Learn Python in One Week
Developer Name: Truston Ailende
Email Address: truston@trustonailende.com
"""
from random import randint

# Generate the first number
first_number = randint(1, 36)

# Generate the second number
second_number = randint(1, 36)

# Ensure that the number is unique
while (first_number == second_number):
    second_number = randint(1, 36)

# Generate the third number
third_number = randint(1, 36)

# Ensure that the number is unique
while ((first_number == third_number) or
	   (second_number == third_number)):
    third_number = randint(1, 36)

# Generate the fourth number
fourth_number = randint(1, 36)

# Ensure that the number is unique
while ((first_number == fourth_number) or
	   (second_number == fourth_number) or
	   (third_number == fourth_number)):
    fourth_number = randint(1, 36)

# Generate the fifth number
fifth_number = randint(1, 36)

# Ensure that the number is unique
while ((first_number == fifth_number) or
	   (second_number == fifth_number) or
	   (third_number == fifth_number) or
	   (fourth_number == fifth_number)):
    fifth_number = randint(1, 36)

# Generate the sixth number
sixth_number = randint(1, 36)

# Ensure that the number is unique
while ((first_number == fifth_number) or
	   (second_number == fifth_number) or
	   (third_number == fifth_number) or
	   (fourth_number == fifth_number) or
	   (fifth_number == sixth_number)):
    sixth_number = randint(1, 36)

# Print out the numbers
print(first_number)
print(second_number)
print(third_number)
print(fourth_number)
print(fifth_number)
print(sixth_number)
