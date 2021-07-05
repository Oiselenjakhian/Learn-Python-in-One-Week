from random import randint

# Generate a number from 1 to 36
number = randint(1, 36)

# Define an empty list
numbers = []

# Create a generator
while len(numbers) < 6:
    if number not in numbers:
        numbers.append(number)
    else:
        pass
    number = randint(1, 36)

# Print the elements of the list
for number in numbers:
    print(number)
