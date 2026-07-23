# Python User Input - Python allows for user input using input(prompt) function
#Example 1
'''print("Enter your Name:")
name= input()
print(name)
print(f"My Name is: '{name}'")'''
#Example 2
#print(input("Enter your name:"))
'''name= input("Enter your name: ")
age= input("Enter your age:")
HomeTown= input("Enter your location:")
print(f"My name is {name}, age is {age} and hometown is {HomeTown}.")'''
#Example 3
# Input from the user is always treated as String. An input string can be converted to number using float() function
import math
'''x= input("Enter a number:")
# Find the square root of the number
y= math.sqrt(float(x))
print(f"The Square root of {x} is {y}")
print(x :=input("Enter number:"))'''
# Input() function with while loop, try:, except: , else:, finally:
y= True
while y== True: 
    x= input("Enter your number:")
    try:
        x= float(x)
        y= False
    except:
        print("Invalid input Entered. Try again.")
    else: print("You have Entered Valid input.Thank You.")

