# Python Bitwise Operators are used to compare two Binary values
# & | ^ ~ << >>
print(6 & 3) # Bitwise AND -> set to 1 if both are 1 otherwise 0
print(6 | 3) # Bitwise OR -> set 1 if both are 1 or different ; set 0 if both are 0
print(6 ^ 3) # Bitwise XOR -> set 0 if both are same.
print(~3) # Bitwise NOT -> Inverts all the bits [0's become 1 and 1's become 0]
print(6<<3) # Bitwise << Left shift y = x*(2**n)
print(6>>3) # Bitwise >> Right shift y = y//(2**n)
#---------------------------------------------------------------
x= print(~3)
x= print(int('0b11',2))
#Bitwise NOT formula ~n=-(n+1)