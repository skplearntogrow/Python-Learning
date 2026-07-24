# Assignment Operators in Python are used to assign values to Variables.
x= 5 # Assignment operator
print(x)
x+=5 # Add and assign
print(x)
x-=5 # subtract and assign
print(x)
x/=4 # Divide and assign
print(x)
x%=4 # Modulus and assign
print(x)
x//=3 # Floor divide and assign
print(x)
x*=4 # Multiply and assign
print(x)
x**=3 # Exponentiate and assign
print(x)
print(x:=4) # Walrus Operator [Assignment expression]
#----------------------------------------------------
# Bitwise Shift Operators
# Bitwise Shift Operators simple formula
# Left shift x*(2 to power of n)
# Right shift x//(2 to power of n)
x= 20
x>>=4 # Right shift and assign
print(x)
x= 20
x<<=4 # left shift and assign
print(x)
#----------------------------------------------------
x= 15
x&=4 # Bitwise AND and assign
# if both bits are different then it is 0
print(x)
x= 15
x|=4 # Bitwise OR and assign
# if both bits are same then value is same, if both bits are different then value will be 1
print(x)
x= 15
x^=4 # Bitwise XOR and assign. XOR is also called as Exclusive OR
# XOR where if both bits are same then consider it as 0
print(x)

#Extra Learning
#-------------------------------------------------------------------
# Convert integer value to binary
y= 4
b= bin(y)
print(b)
# Convert Binary value to Decimal
# Binary value is considered as string in python hence when assigning binary value to variable give "" or ''
# Binary value in python is represented by 0b. Ex: 0b1010 , 0b1111
y= '00100'
d= int(y,2)
print(d)
#-------------------------------------------------------------------
# Walrus Operator example
numbers= [1,2,3,4,5]
if (count:= len(numbers))> 3:
    print(f"List has {count} elements.")
fruits= ["Banana","apple"]
if (count:= len(fruits)) < 3:
    print(f"The Value is {count}.")
else:
    print(f"The List count is less than or equal to 3.")