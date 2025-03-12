# ------------------------------------------LESSON #02 { LISTS, TUPLES & DICTIONARY } --------------------------------------------------------------

#▫️01.LIST 

fruits: list = ["apple", "banana", "cherry"]
numbers: list = [10, 20, 30, 40]
mixed: list = ["hello", 42, 3.14, True]

print("fruits  = ", fruits)
print("numbers = ", numbers)
print("mixed   = ", mixed)

#🔹Accessing List elements

print("First fruit = ", fruits[0])
print("Last number = ", numbers[-1])
print("Last element of mixed = ", mixed[-1])

#🔹Modifying List 

fruits.append("orange")
print("fruits after appending = ", fruits)

fruits.remove("banana")
print("fruits after removing = ", fruits)

#🔹List Slicing

print("fruits[1:3] = ", fruits[1:3])
print("numbers[:3] = ", numbers[:3])
print("mixed[1:]  = ", mixed[1:])

#🔹Sorting List 

fruits.sort()
print("fruits after sorting = ", fruits)

numbers.sort(reverse=True)
print("numbers after sorting in descending order = ", numbers)

#🔹List Comprehension

squares = [x**2 for x in range(1, 11)]
print("Squares of numbers from 1 to 10 = ", squares)

# ------------------------------------------------------------------------------------------------------!!!

#▫️02.TUPLE

fruits_tuple = ("apple", "banana", "cherry")
numbers_tuple = (10, 20, 30, 40)

print("fruits_tuple  = ", fruits_tuple)
print("numbers_tuple = ", numbers_tuple)

#🔸Accessing Tuple elements

print("First fruit = ", fruits_tuple[0])
print("Last number = ", numbers_tuple[-1])

#🔸Tuple Slicing

print("fruits_tuple[1:3] = ", fruits_tuple[1:3])
print("numbers_tuple[:3] = ", numbers_tuple[:3])

#🔸Tuple Unpacking

fruits, numbers = fruits_tuple, numbers_tuple
print("fruits after unpacking = ", fruits)
print("numbers after unpacking = ", numbers)

#🔸Tuple Length

print("Length of fruits_tuple = ", len(fruits_tuple))

#🔸Irretating though tuple

for fruit in fruits_tuple:
    print(fruit)

#🔸Concatenating Tuple

fruits_tuple += ("orange",)
print("fruits_tuple after concatenating = ", fruits_tuple)

#🔸Repeating tuples

repeated_tuple = fruits_tuple * 2
print("repeated_tuple = ", repeated_tuple)

#🔸Nested Tuple

nested_tuple = ("apple", "banana", ("cherry", "orange"))
print("nested_tuple = ", nested_tuple)

# ------------------------------------------------------------------------------------------------------!!!


#▫️03.DICTIONARY

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print("person = ", person)

#🔹Accessing Dictionary elements

print("Name = ", person["name"])
print("Age = ", person["age"])
print("City = ", person["city"])

#🔹Modifying Dictionary

person["age"] = 31
print("person after modifying age = ", person)

person["address"] = "123 Main St"
print("person after adding address = ", person)

#🔹Dictionary Length

print("Length of person = ", len(person))

#🔹Iterating through dictionary

for key in person:
    print(key, "=", person[key])

#🔹Removing dictionary elements

del person["address"]
print("person after deleting address = ", person)

#🔹Dictionary Comprehension

squares_dict = {x: x**2 for x in range(1, 11)}
print("Squares of numbers from 1 to 10 = ", squares_dict)

#🔹Dictionary Sorting

sorted_person = dict(sorted(person.items()))
print("person after sorting = ", sorted_person)

# -------------------------------------------LESSON #02 [ END ]-----------------------------------------------------------









