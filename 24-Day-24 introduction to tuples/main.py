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