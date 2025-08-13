#creating two frozensets
fset1 = frozenset([1,2,3,4,5])
fset2 = frozenset([4,5,6,7,8])

#Union
print("Union:",fset1 | fset2)      # or fset.union(fset2)

#intersection
print("Intersection:",fset1 & fset2)      # or fset.intersection(fset2)

#Difference
print("Difference:",fset1 - fset2)
# or fset1.difference(fset2)


#Subset check
print("Is fset1 a proper subset of fset2?", fset1 < fset2)

#Length
print("Length of fset1:",len(fset1))

#checking membership
print("Is 3 in fset1? : ",3 in fset1)
print("Is 10 in fset1? : ",10 in fset1)
