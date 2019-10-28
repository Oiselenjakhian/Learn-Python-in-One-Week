"""
Project Name: Learn Python in One Week
Developer Name: Truston Ailende
Email Address: truston@trustonailende.com
"""
# Explain the purpose of the program
print("This is a BMI Calculator")

# Ask the user to enter their weight
weight = float(input("Please enter your weight (kg): "))

# Ask the user to enter their height
height = float(input("Please enter your height (m): "))

# Calculate the BMI of the user
BMI = weight / (height * height)

# Round up the BMI to 1 decimal place
BMI = round(BMI, 1)

# Display the BMI
print("Your BMI is: ", BMI)

# Evaluate the BMI based on the BMI Diagnosis Table
if (BMI < 18.5):
    print("Underweight")
elif ((BMI >= 18.5) and (BMI < 25)):
    print("Normal")
elif ((BMI >= 25) and (BMI < 30)):
    print("Overweight")
else:
    print("Obese")
