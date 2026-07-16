# Shortest program to print a random prime number between 1 and 10
# Prime number: A number that can only be divided by 1 and itself.
# Python runs the code from top to bottom.

import random

def is_prime(n):
    return n>1 and all(n%i for i in range(2,int(n**0.5) +1))

while True:
    x= random.randint(1,10)
    if is_prime(x):
        print(x)
        break
