# Find factorial of a given number using while loop

num = int(input("Enter a number: "))

factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(f"The factorial of {num} is: {factorial}")