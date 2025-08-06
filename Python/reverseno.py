# Reverse the given number

num = int(input("Enter a number: "))

reversed_num = 0
temp = abs(num)  # Handle negative numbers

while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10

if num < 0:
    reversed_num = -reversed_num

print(f"The reversed number is: {reversed_num}")