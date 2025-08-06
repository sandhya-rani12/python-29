# Demonstration of common tuple functions in Python

my_tuple = (50, 20, 90, 10, 70, 20)

print("Original tuple:", my_tuple)

# Count occurrences of an element
count_20 = my_tuple.count(20)
print("Count of 20:", count_20)

# Find the index of an element
index_90 = my_tuple.index(90)
print("Index of 90:", index_90)

# Get the length of the tuple
length = len(my_tuple)
print("Length of the tuple:", length)

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing the tuple
print("Slice [1:4]:", my_tuple[1:4])