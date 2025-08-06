# set Declarations
# method 1: Using curly braces {}
set1 = {1,2,3,4}
print("Set1:",set1)

# method 2: Using the set() function
set2 = set([3,4,5,6])
print("Set2:",set2)

# Set Functions

# 1)Union 
union_set = set1.union(set2)
print("Union of Set1 and Set2:", union_set)

# 2)Intersection
intersection_set = set1.intersection(set2)
print("Intersection of Set1 and Set2:", intersection_set)

# 3)Difference
difference_set = set1.difference(set2)
print("Difference (Set1 - Set2):",difference_set)

# 4)Add : an element to set1
set1.add(10)
print("After adding 10 to Set1:",set1)

# 5)Remove : an elemnet from set2
set2.remove(6)
print("After removing 6 from Set2:",set2)

# 6) Check membership
print("Is 2 in Set1", 2 in set1)
print("Is 7 in Set2?",7 in set2)

# Clear the set
set1.clear()
print("Set1 after clear():",set1)