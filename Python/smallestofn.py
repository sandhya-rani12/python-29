# Program to print the smallest of n numbers

n = int(input("Enter how many numbers: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    smallest = float('inf')
    count = 1
    while count <= n:
        num = float(input(f"Enter number {count}: "))
        if num < smallest:
            smallest = num
        count += 1
    print(f"The smallest number among the entered numbers is: {smallest}")