# Creating Global and Local Variables in Python
# In Python, a variable declared outside a function or in the main body of python script is called Global Variable.
# In Python, a variable declared inside a function is called local variable.
# Global Variables can be accessed outside and inside the function. Whereas Local variables can be accessed only in that particular function.
# Python allows to declare a Global variable inside a function using keyword "global".
#Example of Global variable.
x=5
y="Hello"
def myFunction():
    print("This is a Global Variable x value is:",x)
    print(y,x)
    #print("Value of Global Variable x is:"+ x)
myFunction()
m="Hello"
n='World'
def MyFunction():
    print(m+n)
    print(m+" "+n)
MyFunction()
#Creating a variable inside a function with same name as Global Variable.
def My_Function():
    m="Hello World"
    print(m)
My_Function()
print(m)
#To Create Global variable inside a function use global keyword.
def myfun():
    global myName
    myName = "TestCase 1"
    print(myName)
myfun()
print(myName)
# Another example for global keyword usuage within the function
def myName():
    global Name1
    Name1 = "Python is Beautiful language"
myName()
print(Name1)
#Change value of Global variable inside a function
X = "Fantastic"
def My_Function():
    global X
    X = "Excellent"
My_Function()
print("Python is "+X)