# ------------------------------------------LESSON #03 { THE SET & FROZENSET } -------------------------------------------------------------

#🔘.SET
set1 = {1, 2, 3, 4, 5}
set2 = set([4, 5, 6, 7, 8]) 
mixed_set = {"apple", 42, 3.14, True}  

print("set1 =", set1)
print("set2 =", set2)
print("mixed_set =", mixed_set)

#🔹Add elements to a set

set1.add(6)
set2.update([9, 10, 11])

print("After adding elements:")
print("set1 =", set1)

#🔹Remove elements from a set

set1.remove(2)
set2.discard(5)

print("After removing elements:")
print("set1 =", set1)

#🔹Union of two sets

union_set = set1.union(set2)
print("Union of set1 and set2 =", union_set)

#🔹Intersection of two sets

intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2 =", intersection_set)

#🔹Difference of two sets

difference_set = set1.difference(set2)
print("Difference of set1 and set2 =", difference_set)

#🔹Subset check

subset_check = set1.issubset(set2)
print("Is set1 a subset of set2?", subset_check)

#🔹Superset check

superset_check = set2.issuperset(set1)
print("Is set2 a superset of set1?", superset_check)

#🔹Set Length

set_length = len(set1)
print("Length of set1 =", set_length)

#🔹Set Comprehension

even_numbers = {num for num in range(10) if num % 2 == 0}
print("Even numbers in range(10) =", even_numbers)

#------------------------------------------------------------------------------------------------------!!!

#🔘.FROZENSET

frozenset1 = frozenset({1, 2, 3, 4, 5})
frozenset2 = frozenset([4, 5, 6, 7, 8])

print("frozenset1 =", frozenset1)
print("frozenset2 =", frozenset2)

# -------------------------------------------LESSON #03 [ END ]-----------------------------------------------------------

