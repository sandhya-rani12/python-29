# Sum of odd numbers up to n using while loop

n = int(input("Enter the value of n: "))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 2

print(f"The sum of odd numbers up to {n} is: {sum}")