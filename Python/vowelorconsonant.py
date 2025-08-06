# Read a character from the user
char = input("Enter a single alphabet character: ").lower()

# Check if the input is a single alphabet character
if len(char) == 1 and char.isalpha():
    if char in 'aeiou':
        print("The character is a vowel.")
    else:
        print("The character is a consonant.")
else:
    print("Invalid input. Please enter a single alphabet character.")