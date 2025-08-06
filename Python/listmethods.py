# List declaration

# Method 1: Using square brackets []
list1 = [10, 20, 30, 40]
print("List1:", list1)

# Method 2: Using the list() constructor
list2 = list([30, 40, 50, 60])
print("List2:", list2)


#  List Functions

# append(): Add element to the end
list1.append(50)
print("After append(50):", list1)

# extend(): Add multiple elements
list1.extend([60, 70])
print("After extend([60, 70]):", list1)

# insert(): Insert at specific index
list1.insert(2, 25)
print("After insert(2, 25):", list1)

# remove(): Remove specific element
list1.remove(25)
print("After remove(25):", list1)

# pop(): Remove and return last element
popped_item = list1.pop()
print("After pop():", list1)
print("Popped item:", popped_item)

# index(): Get index of first occurrence
print("Index of 30:", list1.index(30))

# count(): Count occurrences
print("Count of 40:", list1.count(40))

# sort(): Sort the list
list1.sort()
print("After sort():", list1)

# reverse(): Reverse the list
list1.reverse()
print("After reverse():", list1)

# copy(): Make a copy of the list
list_copy = list1.copy()
print("Copied list:", list_copy)

# clear(): Remove all items
list1.clear()
print("After clear():", list1)
