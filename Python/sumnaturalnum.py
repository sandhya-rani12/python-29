# Sum of natural numbers up to n using while loop

n = int(input("Enter the value of n: "))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(f"The sum of natural numbers up to {n} is: {sum}")