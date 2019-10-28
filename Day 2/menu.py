"""
Project Name: Learn Python in One Week
Developer Name: Truston Ailende
Email Address: truston@trustonailende.com
"""
# Explain the purpose of the program
print("This is a simple menu application.")

# Display a menu of items
menu = int(input("What do you want to eat?" + 
                 "\n1. Jollof Rice" + 
                 "\n2. Pounded Yam and Egusi" + 
                 "\n3. Yam Porridge" + 
                 "\nPlease make a choice: "))

# Process the user's choice
if (menu == 1):
    print("You chose Jollof Rice.")
elif (menu == 2):
    print("You chose Pounded Yam and Egusi.")
elif (menu == 3):
    print("You chose Yam Porridge.")
else:
    print("Invalid Selection!")
