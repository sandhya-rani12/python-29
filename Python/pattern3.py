n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):  # Loop from n down to 1
    for j in range(65, 65 + i):  # ASCII value of 'A' is 65
        print(chr(j), end=' ')
    print()  # Move to next line
