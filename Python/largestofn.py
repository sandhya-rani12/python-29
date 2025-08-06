# Program to print the largest of n numbers

n = int(input("Enter how many numbers: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    largest = float('-inf')
    count = 1
    while count <= n:
        num = float(input(f"Enter number {count}: "))
        if num > largest:
            largest = num
        count += 1
    print(f"The largest number is: {largest}")