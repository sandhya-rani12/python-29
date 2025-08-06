# list functions in Python

my_list = [5, 2, 9, 1, 7]

print("Original list:", my_list)

# Append an element
my_list.append(4)
print("After append(4):", my_list)

# Insert an element at index 2
my_list.insert(2, 10)
print("After insert(2, 10):", my_list)

# Remove an element
my_list.remove(9)
print("After remove(9):", my_list)

# Pop the last element
popped = my_list.pop()
print("After pop():", my_list, "| Popped element:", popped)

# Sort the list
my_list.sort()
print("After sort():", my_list)

# Reverse the list
my_list.reverse()
print("After reverse():", my_list)

# Find the index of an element
index = my_list.index(7)
print("Index of 7:", index)

# Count occurrences of an element
count = my_list.count(2)
print("Count of 2:", count)

# Get the length of the list
length = len(my_list)
print("Length of the list:", length)