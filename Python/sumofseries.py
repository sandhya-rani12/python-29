import math

# Input: Get the value of n
n = int(input("Enter the value of n: "))

# Initialize the sum with the first term of the series
sum_series = 1

# Loop through odd numbers from 1 to n
for i in range(1, n + 1, 2):
    sum_series += 1 / math.factorial(i)

# Display the result
print("Sum of the series is:", sum_series)
