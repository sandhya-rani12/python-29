# Print Fibonacci series up to n using while loop

n = int(input("Enter the value of n: "))

a, b = 0, 1

while a <= n:
    print(a)
    a, b = b, a + b