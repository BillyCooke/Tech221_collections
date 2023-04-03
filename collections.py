shopping_list = ["milk", "bread", "eggs", "chocolate", "jam"]

print(shopping_list)

# Accessing a particular of the list
print(shopping_list[2])

# change an element
shopping_list[2] = "butter"
print(shopping_list)
print(shopping_list[2])

# Using list methods

# adding to a list with append()
shopping_list.append("fish")
print(shopping_list)

# removing items with remove()
shopping_list.remove("bread")
print(shopping_list)

# removing the last item from a list, without specifying what it is
shopping_list.pop()
print(shopping_list)
shopping_list.pop()
print(shopping_list)

# Can I have a list with mixed data types? - yes
mixture = [1, 2, 3, 4.5, "five", "six"]
print(mixture)

# Slicing
print(mixture[1:3])

# Reverse the order of the slice
print(mixture[-3::])

# Step over
print(mixture[::2])

# Tuples

# Tuples are IMMUTABLE - cannot be changed

tuple_example = ("bread", "eggs", "milk")
print(tuple_example)

# Dictionaries
# Another way to manage data, but are a little bit more dynamic

# Key-Value pairs

# Key = reference to the object
# Value = the data mechanism you wish to store the data in (e.g string, int, list, another dictionary

student_1 = {
    "name": "luke",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_name": ["variables", "data_types", "setup"]
}

# Access the dictionary

print(student_1["stream"])

# Access a part of the list in the dictionary

print(student_1["completed_lesson_name"][2])

# Changing a value in a dictionary
student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

# Changing an element of a list within a dictionary
student_1["completed_lesson_name"].remove("data_types")
print(student_1["completed_lesson_name"])

# Dictionary methods

print(student_1.keys())
print(student_1.values())

# Sets and Frozen sets

# set in python is a list that has no order/indexing

car_parts = {"wheels", "doors", "exhaust"}
print(car_parts)
print(car_parts)
print(car_parts)
print(car_parts)

car_parts.add("windows")
print(car_parts)

car_parts.discard("doors")
print(car_parts)

# Frozen sets are immutable sets

x = frozenset([1, 2, 3, 4])