# Python Operatos Precedence list ranking
print((6+3)-(6+3)) # Parentheses has Highest Precedence in all the Operators
print(100-3**3) # Exponentiation has 2nd Precedence.
print(100+~3) # Uniary +, Uninary -, Bitwise NOT has 3rd Precedence.
print(100+5*3) # Multiplication, division, floor division, modulus has 4th Precendence.
print(100-5*3) # Addition and Subtraction has 5th Precedence.
print(5<<4-3,end="") # Bitwise left and Right shift has 6th Precedence.
print(5>>4-3)
print(6&2+1) # Bitwise AND has 7th Precedence.
print(6|2+1) # Bitwise OR has 8th Precedence.
print(6==4+1,end=",") # Comparison, identity and membership operators has 9th precedence.
print(6!=4-1,end=",")
print(6>4-1,end=",")
print(6>=4-1,end=",")
print(6<4-1,end=",")
print(6<=4-1,end=",")
print((6+4) is 10,end=",")
print((6+4) is not 10,end=",")
print(6+4 in [4,5,6],end=",")
print(6+4 not in [4,5,6])
print(not 5==5) # Logical NOT has 10th Precedence.
print(1 or 2 and 3) # Logical AND has 11th Precedence.
print(1+2 or 3) # Logical OR has 12th Precedence.

# Left to Right Evaluation. if two operators have same precedence then executed left to right
print(5+4-7+3) #5+4 is 9-7=2+3= 5