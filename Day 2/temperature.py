"""
Project Name: Learn Python in One Week
Developer Name: Truston Ailende
Email Address: truston@trustonailende.com
"""
# Explain the purpose of the program
print("This is a Temperature Converter")

# Display a menu for the temperature conversions
menu = int(input("What conversion do you want to perform?" +
                 "\n1. Celsius to Fahrenheit" +
                 "\n2. Fahrenheit to Celsius" + 
                 "\nPlease make a choice: "))

# Convert from Celsius to Fahrenheit
if (menu == 1):
    celsius = float(input("Please enter a value in Celsius: "))
    fahrenheit = ((celsius * 9) / 5)  + 32
    print(str(celsius) + chr(176) + "C",
          " is", str(round(fahrenheit, 2)) + chr(176) + "F")

# Convert from Fahrenheit to Celsius
elif (menu == 2):
    fahrenheit = float(input("Please enter a value in Fahrenheit: "))
    celsius = ((fahrenheit -32) * 5) / 9
    print(str(round(fahrenheit, 2)) + chr(176) + "F",
          " is", str(celsius) + chr(176) + "C")

else:
    print("Invalid Selection")
