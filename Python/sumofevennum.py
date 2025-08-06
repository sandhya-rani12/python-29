# Sum of even numbers up to n using while loop

n = int(input("Enter the value of n: "))

sum = 0
i = 2

while i <= n:
    sum += i
    i += 2

print(f"The sum of even numbers up to {n} is: {sum}")