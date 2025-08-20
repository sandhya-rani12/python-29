
# Creating an array 
arr = [10, 20, 30, 40, 50,60]
print("Initial Array:", arr)

# 1. Append 
arr.append(60)
print("After Append:", arr)

# 2. Insert 
arr.insert(2, 25)   
print("After Insert:", arr)

# 3. Remove 
arr.remove(40)
print("After Remove (40):", arr)

# 4. Delete 
arr.pop(3)   
print("After Pop at index 3:", arr)

# 5. Find index of an element
print("Index of 10:", arr.index(10))

# 6. Count occurrences of an element
print("Count of 20:", arr.count(20))

# 7. Reverse the array
arr.reverse()
print("After Reverse:", arr)

# 8. Sort the array
arr.sort()
print("After Sort:", arr)

# 9. Length of array
print("Length of Array:", len(arr))

# 10. Slicing the array
print("Array Slice (first 3 elements):", arr[:3])

# 11. Extend array with another list
arr.extend([70, 80, 90])
print("After Extend:", arr)

# 12. Clear the array
arr.clear()
print("After Clear:", arr)

