'''
Question 3: Nested Age Check
Description: Write a program that checks a person’s age and prints a message. The program should have the following logic:

If the person is below 13, print "Child".
If the person is between 13 and 19, print "Teenager".
If the person is between 20 and 64, print "Adult".
If the person is 65 or older, print "Senior".
If the person’s age is 18 or 21, print "Young Adult".
'''

# This program will check age categories
while True:
    try:
        age = int(input("Enter your age: "))
        
        if age != None:
            break

    except ValueError:
        print("\nThat is not a valid age number! Please try again.\n")

# Add if-elif-else logic here with nested conditions
if age < 13:
    print("\nChild")

elif age >= 13 and age <= 19:
    # First Nested if/else statement.
    if age != 18:
        print("\nTeenager")
    elif age == 18:
        print("\nYoung Adult")

elif age >= 20 and age <= 64:
    # Second Nested if/else statement.
    if age != 21:
        print("\nAdult")
    elif age == 21:
        print("\nYoung Adult")

elif age >= 65:
    print("\nSenior")