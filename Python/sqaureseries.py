# Print the series: 1 2 4 8 16 32 ... n^2

n = int(input("Enter the value of n: "))

i = 1
while i <= n * n:
    print(i, end=" ")
    i *= 2
print()