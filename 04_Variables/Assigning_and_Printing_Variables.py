#Python allows you to assign multiple values to multiple variables in one line.
x,y,z = 5,"Hello",3.14
print(x)
print(y)
print(z)
myVariablename,MyVariableName,MY_Variable_Name = 50, 100, 500
print(type(myVariablename))
print(myVariablename)
print(MyVariableName)
print(MY_Variable_Name)
#m,n,o = 1,2,3,4 #Output was error: too  many values to unpack (expected 3)
#print(m)
#print(n)
#print(o)
#Assigning One value to Multiple Variables.
a=b=c= 50
d=e=f="Test 1"
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
#Unpacking a Collection.
mylist = ["apple","banana","cherry"]
x,y,z = mylist
print(x)
print(y)
print(z)
#unpacking a Tuple.
mytuple =("apple","banana","Orange")
tuple1,tuple2,tuple3 = mytuple
print(tuple1)
print(tuple2)
print(tuple3)
#Output variables
#you can output variables using the print() function.
#Using print() function you can output multiple variables seperated by comma.
r="Hello"
s="World"
t= 2026
print(r,s,t)
testCase = "This is a Test Case"
TestCase = "for testing the output of"
Test_Case = "multiple variables seperated by comma using print() function."
print(testCase,TestCase,Test_Case)
# We can also use the + Operator to output multiple variables.
#However, when using the + operator, you need to make sure that all variables are of the same type, or you will get an error.
print(r + s + str(t))
print(testCase+TestCase+Test_Case)
Jim = 5
jim = 10
_jim = 15
print(Jim+jim+_jim)
x=5
y="5"
print(x+int(y))