# Simple Python code for slicing a string

text = "Hello, World!"

# Slice from index 0 to 4 (excluding 5)
print("text[0:5] =", text[0:5])  # Output: Hello

# Slice from start to index 4
print("text[:5] =", text[:5])    # Output: Hello

# Slice from index 7 to the end
print("text[7:] =", text[7:])     # Output: World!

# Slice the whole string
print("text[:] =", text[:])      # Output: Hello, World!

# Slice with step (every second character)
print("text[::2] =", text[::2])  # Output: Hlo ol!

# Negative indexing (last 6 characters)
print("text[-6:] =", text[-6:])  # Output: World!
