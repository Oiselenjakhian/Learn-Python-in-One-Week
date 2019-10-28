"""
Project Name: Learn Python in One Week
Developer Name: Truston Ailende
Email Address: truston@trustonailende.com
"""
# Assign variables for the PIN and account balance
PIN = 1234
account_balance = 1000000

# Welcome the user
print("Welcome to TrustBank")

# Ask the user to enter a PIN
input_pin = int(input("Please enter your PIN: "))

# Ensure the PINs match as the looping condition
while (input_pin == PIN):
    # Display a menu of options
    menu = int(input("\nWhat do you want to do?" +
                     "\n1. Withdraw N20,000" +
                     "\n2. Check Account Balance" +
                     "\n3. End Transaction" +
                     "\nPlease select an entry: "))

    # Withdraw N20,000
    if (menu == 1):
        # Subtract from the account balance
        account_balance = account_balance - 20000

        # Ask the user if they want to perform another transaction
        option = int(input("\nDo you want to perform another transaction" +
                           "\n1. Yes" +
                           "\n2. No" +
                           "\nPlease select an option: "))

        # If the user want to perform another transaction, ask for their PIN
        if (option == 1):
            input_pin = int(input("Please enter your PIN: "))

            # If the PIN is correct, exit and go back to the menu
            if (input_pin == PIN):
                continue
            # Else end the program
            else:
                break
        # End the program
        elif (option == 2):
            print("Thank you for banking with us.")
            break
        # End the program
        else:
            print("Invalid Selection!")
            break

    # Display the account balance
    elif (menu == 2):
        print("Your account balance is:", account_balance)

        # Ask the user if they want to perform another transaction
        option = int(input("\nDo you want to perform another transaction" +
                           "\n1. Yes" +
                           "\n2. No" +
                           "\nPlease select an option: "))

        # If the user want to perform another transaction, ask for their PIN
        if (option == 1):
            input_pin = int(input("Please enter your PIN: "))

            # If the PIN is correct, exit and go back to the menu
            if (input_pin == PIN):
                continue
            # Else end the program
            else:
                break
            
        # End the program
        elif (option == 2):
            print("Thank you for banking with us.")
            break
        
        # End the program
        else:
            print("Invalid Selection!")
            break
        
    # Once the user ends the transaction, exit the loop
    elif (menu == 3):
        print("Thank you for banking with us.")
        break

    # If there is an invalid selection, exit the loop
    else:
        print("Invalid Selection!")
        break
# If the PINs don't match come here
else:
    print("Invalid PIN")

print("\nPlease have a good day.")
