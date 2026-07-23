# Python None constant
x= None
print(x)
print(type(x))
# Comparing to None using identity operators is or is not
result= None
if result is None:
    print("There is No Result.All the Best.")
else: print("You got the Result.")
area= None
if area is not None:
    print("You know the location.")
else: print("You dont know the location.")
# None evaluates to False in boolean context
print(bool(area))
print(bool(None))
# Function returning None. Functions that do not explicitly return a value return None.
def myfun():
    x=5
    #return 5
x= myfun()
print(x)