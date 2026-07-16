# This is a chapter to learn, practice Numeric types in Python language with examples.
# Variables of numeric type are created when you assign value to them
x= 1 #int
y= 2.9 #float
z= 1+2j #complex
print(type(x))
print(type(y))
print(type(z))
# int or Integer is a whole number without a decimal, with unlimited length and can be postive or negative.
x= 1
y= 23456789
z= -250
print(type(x))
print(type(y))
print(type(z))
# float or Float point number is a decimal number that can be positive or negative containing one ore more decimals.
x= 1.5
y = -5.0
z = -28907.98706
m = 253.7e10 # scientific number with e to indicate power of 10
print(type(x))
print(type(y))
print(type(z))
print(type(m))
# complex numbers are written with "j" as imaginary part.
x= 2j
y= -23j
z= 5+6j
print(type(x))
print(type(y))
print(type(z))
# Type Conversion: We can convert one type to another with int(),float() and complex() methods.
x = 1 #integer
y= 2.8 #float point number
z = 1j # complex number
a = float(x) # converting integer to float pointing number
b = int(y) # converting float to integer
c = complex(x) # converting integer to complex number
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
# We cannot convert complex number to another numeric type.

