'''
Question 1: Weather Alert System

Description: Write a program that takes a temperature input from the user and prints whether the weather is hot, cold, or moderate. If the temperature is above 30°C, print "Hot". If it's below 10°C, print "Cold". Otherwise, print "Moderate". If the temperature is exactly 25°C, print "Perfect weather!".
'''

# This program will check the temperature and give a weather update
while True:
    try:
        temperature = float(input("Enter the temperature in °C: "))

        if temperature != None:
            break

    except ValueError:
        print("\nInvalid Temperature Value! Please try again.\n")


# Complete the if-elif-else logic here

if temperature <= 5:
    print(f"\nThe weather is {temperature:.2f} °C outside right now. It is freezing!")

elif temperature < 32 and temperature > 5:
    print(f"\nThe weather is {temperature:.2f} °C outside right now. It is chilly, maybe even warm!")

else:
    print(f"\nThe weather is {temperature:.2f} °C outside right now. It is pretty warm!")