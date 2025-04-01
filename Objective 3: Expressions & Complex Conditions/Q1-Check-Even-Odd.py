'''
Question 1: Check for Even or Odd
Description: Write a program that takes an integer as input and checks if it's even or odd using a combination of relational and logical operators.
'''

# This program will check if the input number is even or odd
while True:
    try:
        number = int(input("Enter a number: "))

        if number != None:
            break

    except ValueError: 
        print("That is not a valid integer! Please try again.")

# Use relational and logical operators to check for even/odd & Print out which it is to the terminal
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
elif number % 2 != 0:
    print(f"\nThe number {number} is odd.")