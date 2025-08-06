import math

# Input x (angle in radians) and n (highest term exponent)
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the highest even exponent n: "))

# Initialize sum and sign
cos_x = 0
sign = 1

# Loop through even terms: 0, 2, 4, ..., n
for i in range(0, n + 1, 2):
    term = sign * (x**i) / math.factorial(i)
    cos_x += term
    sign *= -1  # alternate signs

# Output the result
print("Cosine of x using series =", cos_x)
