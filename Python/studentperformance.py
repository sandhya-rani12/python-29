# Read percentage from the user
percentage = float(input("Enter the student's percentage: "))

# Check performance based on percentage
if percentage >= 90:
    print("Excellent performance")
elif percentage >= 80:
    print("Very good performance")
elif percentage >= 70:
    print("Good performance")
elif percentage >= 60:
    print("Average performance")
else:
    print("Poor performance")