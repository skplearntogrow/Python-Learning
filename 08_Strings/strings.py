# In this file we will do coding practice for Pythong Strings fundamentals
Test= "This Test Case is Passed" # Assigning String to a Varible.
print('This Test Case is Passed') # Single Quote.
print("This Test Case is Passed") # Double Quote.
print('This Test Case is "Passed"') # Double Quote inside single quote.
print("This Test Case is 'Passed'") # Single Quote inside Double quote.
Test1= """Validate Login Functionality of the site
using edge cases and
also perform field and page level Validations""" # Double quotations used in a Multiline string and assigned to a variable.
Test2= '''Validate Page rendering functionality of the site
using edge cases and also check for LCP value of the site''' # Single quotations used in a Multiline string and assigned to a variable.
print(Test1)
print(Test2)
# Strings are Arrays. in Python we dont have character(char) data type hence a string is an array of unicode characters
print(Test[0],end=",")
print(Test[1])
# Remember that the first character in a String has a position 0.
#Looping through a String. Since Strings are arrays, we can loop through a string using for loop
for x in "Banana": # Loop through the letters in the word "Banana"
    print(x)
for x in Test:
    print(x)
