n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):         # Loop from 1 to n
    for j in range(i):            # Print i, i times
        print(i, end=' ')
    print()  # Move to next line
