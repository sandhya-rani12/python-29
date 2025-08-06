# Read two numbers from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Compare the numbers and print the largest
if a > b:
    print("The largest number is:", a)
elif b > a:
    print("The largest number is:", b)
else:
    print("Both numbers are equal.")
