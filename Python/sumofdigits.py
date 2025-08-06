# Find sum of digits of a given number

num = int(input("Enter a number: "))

sum_digits = 0
temp = abs(num)  # Handle negative numbers

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    temp //= 10

print(f"The sum of digits of {num} is: {sum_digits}")