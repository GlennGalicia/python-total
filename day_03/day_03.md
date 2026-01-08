## 📘 Day 3

### String Methods

```py
sample_str = " Hello, Python World! "

# Find index of character 'H'
character1 = sample_str.index('H')  # 0

# Find index of substring 'Python'
character2 = sample_str.index('Python')  # 7

# Find index of character 'o' starting from index 5
character3 = sample_str.index('o', 5)  # 8 (searching from index 5)

# Find last index of character 'o' 
character4 = sample_str.rindex('o', 10)  # 17 (searching backwards up to index 10)

# Find index of character 'z' (not found)
character5 = sample_str.find('z')  # -1 (not found)

# Convert to uppercase
upper_str = sample_str.upper()  # " HELLO, PYTHON WORLD! "

# Convert to lowercase
lower_str = sample_str.lower()  # " hello, python world! "

# Convert sentence from string to list of characters
char_list = list(
    sample_str)  # [' ', 'H', 'e', 'l', 'l', 'o', ',', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', 'W', 'o', 'r', '

# Remove leading and trailing whitespace
stripped_str = sample_str.strip()  # "Hello, Python World!"

# Replace substring
replaced_str = sample_str.replace("Python", "Java")  # " Hello, Java World! "

# Join list of strings into a single string
str_list = ["Hello", "from", "Python"]
joined_str = " ".join(str_list)  # "Hello from Python"
```

### Slice Strings

```py
sample_str = "Hello, Python World!"

# Slice from index 0 to 5
slice1 = sample_str[0:5]  # "Hello"

# Slice from index 7 to end
slice2 = sample_str[7:]  # "Python World!"

# Slice from start to index 5
slice3 = sample_str[:5]  # "Hello"

# Slice with step
slice4 = sample_str[::2]  # "Hlo yhnWrd"
```

### Lists

Is a collection which is ordered and changeable(modifiable). Allows duplicate members.
A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.

```py
sample_list = [5, 2, 9, 1, 5, 6]

# Append an element
sample_list.append(10)  # [5, 2, 9, 1, 5, 6, 10]

# Remove an element. The remove method removes a specified item from a list
sample_list.remove(2)  # [5, 9, 1, 5, 6, 10]

# Pop an element at index 1. The pop() method removes the specified index, (or the last item if index is not specified):
popped_element = sample_list.pop(1)  # popped_element=9, sample_list

# Removing Items Using Del
del sample_list[0:2]  # sample_list = [1, 5, 6, 10]

# Insert an element at index 2
sample_list.insert(2, 7)  # [1, 5, 7, 6, 10]

# Search for an element's index
index_of_5 = sample_list.index(5)  # 1

# Count occurrences of an element
count_of_5 = sample_list.count(5)  # 1

# Unpack list into variables
a, b, c, d, *rest = sample_list  # a=1, b=5, c=7, d=6, rest=[10]

# Checking Items in a list
is_five_in_list = 5 in sample_list  # True
is_twenty_in_list = 20 in sample_list  # False

# Copy the list
copied_list = sample_list.copy()  # [1, 5, 7, 6, 10]

# Joining list with plus operator (+) or extend() method

# plus operator
another_list = sample_list + copied_list  # [1, 5, 7, 6, 10, 1, 5, 7, 6, 10]

# extend() method
sample_list.extend(copied_list)  # [1, 5, 7, 6, 10, 1, 5, 7, 6, 10]

# Slice the list
sliced_list = copied_list[2:5]  # [7, 6, 10]

# Clear the list
sample_list.clear()  # []

# Sort the list ascending
sample_list.sort()  # [1, 5, 6, 7, 10]

# Sort the list descending
sample_list.sort(reverse=True)  # [10, 7, 6, 5, 1]

# Reverse the list
sample_list.reverse()  # [10, 6, 7, 5, 1]

# Get the length of the list
list_length = len(sample_list)  # 6

# Iterate through a list using a for loop
for item in sample_list:
    print(item)  # prints each item in the list
```

### Dicctionaries

A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written

```py
sample_dict = {
    "name": "Alice",
    "last_name": "Smith",
    "age": 30,
    "city": "New York",
    "is_student": False
}

# Checking the type of dictionary
type(sample_dict)  # <class 'dict'>

# Length of dictionary
dict_length = len(sample_dict)  # 3

# Accessing values
name = sample_dict["name"]  # "Alice"

# The get method returns None, which is a NoneType object data type, if the key does not exist.
age1 = sample_dict.get("age")  # 30

# Adding a new key-value pair
sample_dict["job"] = "Engineer"  # {"name": "Alice", "last_name":"Smith","age": 30, "city": "New York", "job": "Engineer"}

# Removing Key and Value Pairs from a Dictionary

# pop(key): removes the item with the specified key name:
sample_dict.pop("city")  # {"name": "Alice", "age": 30, "job": "Engineer"}

# popitem(): removes the last item
sample_dict.popitem()  # {"name": "Alice", "age": 30}

# del: removes an item with specified key name
del sample_dict["last_name"]  # {"name": "Alice", "age": 30, "job": "Engineer"}

# Using pop() method to remove a key-value pair
age2 = sample_dict.pop("age")  # age=30, sample_dict={"name": "Alice", "job": "Engineer"}

# Getting all keys
keys = sample_dict.keys()  # dict_keys(['name', 'job'])

# Getting all values
values = sample_dict.values()  # dict_values(['Alice', 'Engineer'])

# Getting all items
items = sample_dict.items()  # dict_items([('name', 'Alice'), ('job', 'Engineer')])

# Copying the dictionary
copied_dict = sample_dict.copy()  # {"name": "Alice", "job": "Engineer"}

# Clearing the dictionary
sample_dict.clear()  # {}

# Iterating through a dictionary
for key, value in copied_dict.items():
    print(f"{key}: {value}")  # prints each key-value pair
```

### Tuples

A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:

* `tuple():` to create an empty tuple
* `count():` to count the number of a specified item in a tuple
* `index():` to find the index of a specified item in a tuple
* `operator:` to join two or more tuples and to create a new tuple

```py
# Creating a tuple
sample_tuple = (1, 2, 3, 4, 5)

# Checking the type of tuple
type(sample_tuple)  # <class 'tuple'>

# Length of tuple
tuple_length = len(sample_tuple)  # 5

# Accessing elements
first_element = sample_tuple[0]  # 1

# Counting occurrences
count_of_2 = sample_tuple.count(2)  # 1

# Finding index
index_of_3 = sample_tuple.index(3)  # 2

# Joining tuples
another_tuple = (6, 7, 8)
joined_tuple = sample_tuple + another_tuple  # (1, 2, 3, 4, 5, 6, 7, 8)

# Slicing tuple
sliced_tuple = sample_tuple[1:4]  # (2, 3, 4)

# Changing Tuples to Lists
# We can change tuples to lists and lists to tuples. Tuple is immutable if we want to modify a tuple we should change it to a list.
tuple_as_list = list(sample_tuple)  # [1, 2, 3, 4, 5]
tuple_as_list.append(6)  # [1, 2, 3, 4, 5, 6]
modified_tuple = tuple(tuple_as_list)  # (1, 2, 3, 4, 5, 6)

# Checking an Item in a Tuple
validation = 10 in sample_tuple  # False

# Deleting a Tuple
del joined_tuple  # sample_tuple is deleted

# Iterating through a tuple
for item in sample_tuple:
    print(item)  # prints each item in the tuple
```

### Sets

Set is a collection of unordered and un-indexed distinct elements. In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.

```py
# Creating a set
sample_set = {1, 2, 3, 4, 5}

# Checking the type of set
type(sample_set)  # <class 'set'>

# Length of set
set_length = len(sample_set)  # 5

# Adding an element
sample_set.add(6)  # {1, 2, 3, 4, 5, 6}

# Checking an Item in a Set
is_three_in_set = 3 in sample_set  # True
is_ten_in_set = 10 in sample_set  # False

# Add multiple items using update() The update() allows to add multiple items to a set. The update() takes a list argument.
sample_set.update([7, 8, 9])  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Removing an element with remove(). The remove() method removes the specified item from the set.
sample_set.remove(3)  # {1, 2, 4, 5, 6, 7, 8, 9}

# The pop() methods remove a random item from a list and it returns the removed item.
popped_element = sample_set.pop()  # popped_element=1, sample_set={2, 4, 5, 6, 7, 8, 9}

# Union of sets
another_set = {5, 6, 7, 8}
union_set = sample_set.union(another_set)  # {1, 2, 4, 5, 6, 7, 8}

# Deleting a Set
del union_set  # another_set is deleted

# Converting List to Set
# We can convert list to set and set to list. Converting list to set removes duplicates and only unique items will be reserved.
# Converting List to Set
fruits = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
fruit_set = set(fruits)  # {'banana', 'orange', 'mango', 'lemon'}

# Intersection of sets. Intersection returns a set of items which are in both the sets.
intersection_set = sample_set.intersection(another_set)  # {5, 6}

```

[<< Day 2](../day_02/day_02.md) | [Day 4 >>](../day_04/day_04.md)
