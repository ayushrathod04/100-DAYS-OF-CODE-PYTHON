tuple1 = ("apple", "banana", "cherry")
tuple2= ("orange", "kiwi", "melon")
# Concatenating tuples
tuple3 = tuple1 + tuple2
# Repeating tuples
tuple4 = tuple1 * 2 
# Accessing elements
first_element = tuple1[0]
# Slicing tuples
tuple_slice = tuple1[1:3]
# Checking if an item exists in a tuple
item_exists = "banana" in tuple1
# Finding the length of a tuple
tuple_length = len(tuple1)
# Finding the index of an item
item_index = tuple1.index("banana")
# Counting occurrences of an item
item_count = tuple1.count("banana")
# Converting a list to a tuple
list1 = ["apple", "banana", "cherry"]
tuple_from_list = tuple(list1)
# Converting a tuple to a list
list_from_tuple = list(tuple1)
# Iterating through a tuple
for item in tuple1:
    print(item)     
# Unpacking a tuple
fruit1, fruit2, fruit3 = tuple1         
print(fruit1, fruit2, fruit3)
# Nested tuples
nested_tuple = (tuple1, tuple2)
# Accessing elements in a nested tuple
nested_first_element = nested_tuple[0][0]  # Accessing "apple" from nested_tuple
print(nested_first_element) 
# Tuple methods
# Tuples are immutable, so they do not have methods like append, remove, or pop.
# However, you can use the built-in functions like min, max, and sum on tuples
# Finding the minimum, maximum, and sum of a tuple
# Note: These functions only work with tuples containing numeric values.
numeric_tuple = (1, 2, 3, 4, 5)
min_value = min(numeric_tuple)
max_value = max(numeric_tuple)  
sum_value = sum(numeric_tuple)  
print(f"Min: {min_value}, Max: {max_value}, Sum: {sum_value}")
# Tuple comprehension (similar to list comprehension)
tuple_comprehension = tuple(x * 2 for x in numeric_tuple)
print(tuple_comprehension)  # Output: (2, 4, 6, 8, 10)
# Tuple unpacking with asterisk
tuple_unpacking = (1, 2, 3, 4, 5)
first, *rest = tuple_unpacking
print(first)  # Output: 1
print(rest)   # Output: [2, 3, 4, 5]
# Tuple with a single element (note the comma)
# This is necessary to differentiate it from a regular parenthesis
single_element_tuple = (42,)    
print(single_element_tuple)  # Output: (42,)
# Tuple with mixed data types   
# Tuples can contain elements of different data types       
# This is useful for grouping related data together         
# For example, a tuple representing a person's information          
# could include their name, age, and height     
# Here's an example of a mixed data type tuple:         
# person_info = ("Alice", 30, 5.5)
# You can access the elements of this tuple just like any other tuple:
#   print(person_info[0])  # Output: Alice
#  print(person_info[1])  # Output: 30          
# print(person_info[2])  # Output: 5.5
# # Tuples are often used to return multiple values from a function
# # For example, a function that calculates the area and perimeter of a rectangle
# # could return a tuple containing both values:
# def rectangle_properties(length, width):
#     area = length * width            
