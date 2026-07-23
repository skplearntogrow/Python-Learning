# Python Identity Operators
# Identity operators are used to compare objects not if they are equal but if they are identitical/same with same memory location.
# is is not
# is operator returns True if both variables point to same object
x= ["apple","banana"]
y= ["apple","banana"]
z=x
print(x is z)
print(x is y)
print(x==y)
# is not operator returns True if both variables do not point to same object.
print(x is not z)
print(x is not y)
print(x==y)
# is checks if both variables are pointing to same object in memory.
#== checks if values of both variables are same.
#== check for value where as "is" check for pointing to same object in memory.