"""
Project Name: Learn Python in One Week
Developer Name: Truston Ailende
Email Address: truston@trustonailende.com
"""
# Ask the user for the coefficient of a
coeff_a = float(input("Please enter the value of a: "))

# Ask the user for the coefficient of b
coeff_b = float(input("Please enter the value of b: "))

# Ask the user for the coefficient of c
coeff_c = float(input("Please enter the value of c: "))

# Calculate the value of the discriminant
discriminant = coeff_b**2 - 4*coeff_a*coeff_c

# Use the discriminant as a basis of finding the roots
if (discriminant > 0):
    print("Unique Roots")
    # Square the discriminant
    square_d = discriminant ** 0.5

    # Find the value of x1
    x1 = (-coeff_b + square_d) / 2 * coeff_a

    # Find the value of x2
    x2 = (-coeff_b - square_d) / 2 * coeff_a

    # Print the values of x1 and x2
    print(x1, "and", x2)
elif (discriminant == 0):
    print("Double Roots")

    # Find the value of x
    x = -coeff_b / 2 * coeff_a

    # Print the value of x
    print(x)
else:
    print("Complex Roots")
