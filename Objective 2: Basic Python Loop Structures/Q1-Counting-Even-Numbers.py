'''
Question 1: Counting Even Numbers

Description: Write a program that counts how many even numbers there are in a list of numbers (from 1 to 20).
'''

# This program will count even numbers in a list

numbers = list(range(1, 21))
even_count = 0


# Loop through the numbers and check for even numbers
for numbers in list(range(1, 21)):
    if numbers % 2 == 0:
        even_count += 1
        
print(f"\nThere are {even_count} even numbers counted from the 'numbers' list")