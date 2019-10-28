"""
Project Name: Learn Python in One Week
Developer Name: Truston Ailende
Email Address: truston@trustonailende.com
"""
def grader(score):
    if ((score > 100) or (score < 0)):
        return ("Invalid")
    # If the score is from 90 - 100, display A
    elif ((score >= 90) and (score <= 100)):
        return ("A")
    # If the score is from 80 - 89, display B
    elif ((score >= 80) and (score < 90)):
        return ("B")
    # If the score is from 70 - 79, display C
    elif ((score >= 70) and (score < 80)):
        return ("C")
    # If the score is from 60 - 69, display D
    elif ((score >= 60) and (score < 70)):
        return ("D")
    # If the score is from 50 - 59, display E
    elif ((score >= 50) and (score < 60)):
        return ("E")
    # If the score is from 0 - 49, display F
    else:
        return ("F")

# Ask the user to enter their score
score = int(input("Please enter a score: "))

# Display a grade
print("Your score is:", grader(score))
