# Python Ternary opeator. Assign one value if a condition is True and another value if condition is false
num= 6
x= "Weekend!" if num> 5 else "Workday"
print(x)
x= 90
y= "Distinguished" if x> 90 else "Excellent" if x>70 & x<=90 else "Good" if x>50 & x<=70 else "Poor"
print(y)