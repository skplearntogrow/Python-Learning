# Booleans in Python - True or False
# To know if an expression or a statement is True or False.
# When you compare two values , python responds with True or False
print(10>9)
print(10==10)
print(10<9)
# Booleans in If statement
a= 200
b= 33
if b>a:
    print("b is greater than a")
else: 
    print("b is less than a")
print(f"Multiplication of a*b is {a*b}")
# bool() function evaluates any value and provide response either True or False
print(bool(b))
print(bool(a))
print(bool(50*40))
# Evaluate two variables
x= "Hello"
y= 50
print(bool(x))
print(bool(y))
print(bool("abc"))
print(bool(123))
print(bool(["apple","Mango","Orange"]))
# Some values are False
x= bool(False)
y= bool()
z= bool({})
a= bool(0)
b= bool(None)
c= bool(())
d= bool([])
e= bool("")
f= bool('')
print(x,y,z,a,b,c,d,e,f)
# An object that is made from a Class with a _len_ function that return 0 or False.
class myclass():
    def _len_(self):
        return 0

myobj = myclass()
print(bool(myobj))
# Functions that can return a Boolean value
def myfun():
    return True
print(myfun())
def myfun1():
    return False
print(myfun1())
if myfun():
    print("Yes")
else:
    print("No")
# Any Python built-in function that start with is such as isalpnum() returns either True or False [Boolean values]
# isinstance() function : This function is used to determine if an object is of a certain data type.
x=500
print(isinstance(x,int))
# isinstance is a function that is used to determine if an object is of a certain data type.
print(isinstance(myobj,float))
print(isinstance(f,bool))
print(isinstance(a,float))