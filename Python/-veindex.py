text = input("Enter any string: ")

print("Negative Indexing:")
for i in range(-1, -len(text)-1, -1):
    print(f"index [{i}]: {text[i]}")
