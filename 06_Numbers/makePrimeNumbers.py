# This line is a comment. It explains what the program does, but Python ignores it.
# The program will generate a random prime number between 1 and 50.

import random  # Import the random module so we can generate random numbers

def is_prime(n):  # Define a function named is_prime that checks whether a number is prime
    if n < 2:  # If the number is less than 2, it cannot be prime
        return False  # Return False because it is not prime

    for i in range(2, int(n ** 0.5) + 1):  # Check possible divisors from 2 up to the square root of n
        if n % i == 0:  # If n can be divided evenly by i, then it is not prime
            return False  # Return False

    return True  # If no divisor was found, the number is prime

def random_prime():  # Define a function that keeps trying random numbers until it finds a prime
    while True:  # Repeat forever until we find a prime number
        num = random.randint(1, 50)  # Pick a random number between 1 and 50
        if is_prime(num):  # Check if the random number is prime
            return num  # If it is prime, return it

print(random_prime())  # Call the function and print the random prime number

# Prime numbers are whole numbers that cannot be divided evenly by any other number except 1 and number itself.