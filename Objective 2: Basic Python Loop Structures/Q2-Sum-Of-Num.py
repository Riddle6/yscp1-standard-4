'''
Question 2: Sum of Numbers in a List
Description: Write a program that takes a list of numbers and calculates the sum of all the numbers using a for loop. The program should print the total sum at the end.
'''

# This program will calculate the sum of numbers in a list

numbers = [10, 20, 30, 40, 50]  # List of numbers

# Initialize a variable to hold the sum
total_sum = 0

# Use a for loop to iterate through the numbers
for numbers in numbers:
    total_sum += numbers
    
print(f"\nTotal sum of the numbers from the 'numbers' list is {total_sum}.")