'''
Question 2: Student Performance
Description: Write a program that checks if a student has passed or failed based on two conditions:

The student's grade must be 65 or higher.
The student must have attended more than 75% of the classes.
'''

# This program checks if a student passes based on grade and attendance
while True:
    try:
        grade = float(input("Enter your grade: "))
        
        attendance = float(input("Enter your attendance percentage: "))

        if attendance != None and grade != None:
            break

    except ValueError:
        print("\nInvalid grade and/or attendance. Please enter a number or float.\n")

# Use complex conditions to determine if the student passed
if grade >= 65 and attendance >= 75: # If Grade and Attendance is above 65 and 75%7
    print("\nThis student has passed.")

# First Condition: if Grade and Attendance are BELOW 65 and 75%
# Second Condition: if Grade is ABOVE 65 but Attendance is BELOW 75%
# Third Condition: if Grade is BELOW 65 but Attendance is ABOVE 75%
elif grade < 65 and attendance < 75 or grade >= 65 and attendance < 75 or grade < 65 and attendance >= 75:
    print("\nThis student has failed.")