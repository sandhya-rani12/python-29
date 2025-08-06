# Check if a number is palindrome or not

num = int(input("Enter a number: "))

original = abs(num)
reversed_num = 0
temp = original

while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10

if original == reversed_num:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")