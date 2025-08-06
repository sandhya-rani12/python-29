import math

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Input a number
n = int(input("Enter a number: "))

# Compute square root
sqrt_n = math.sqrt(n)

# Check if square root is integer
if sqrt_n.is_integer():
    if is_prime(int(sqrt_n)):
        print("Square root is prime.")
    else:
        print("Square root is not prime.")
else:
    print("Square root is not an integer, so can't be prime.")
