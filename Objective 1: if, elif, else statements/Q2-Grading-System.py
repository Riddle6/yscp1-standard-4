'''
Question 2: Grading System
Description: Write a program that takes a student's score as input and assigns a grade based on the following criteria:

90 or above: "A"
80-89: "B"
70-79: "C"
60-69: "D"
Below 60: "F"
'''

# This program will assign grades based on the score
while True:
    try:
        score = float(input("Enter the student's score: "))

        if score != None:
            break

    except ValueError:
        print("Invalid Grade! Please try again.")

# Complete the if-elif-else logic to assign grades
if score >= 90:
    print(f"\nYour grade was a {score}. You got an A!")

elif score >= 80 and score <= 89.9:
    print(f"\nYour grade was a {score}. You got a B!")

elif score >= 70 and score <= 79.9:
    print(f"\nYour grade was a {score}. You got a C.")

elif score >= 60 and  score <=69.9:
    print(f"\nYour grade was a {score}. You got a D.")

elif score < 60:
    print(f"\nYour grade was a {score}. You got an F for Failure!")
