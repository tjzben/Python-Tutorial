# A tuple is a collection which is ordered and immutable.
# Allows duplicate members.
# A tuple is created by placing all the items (elements) inside parentheses (), separated by commas.
# The parentheses are optional, however, it is a good practice to use them.

# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple) # ()

# Tuples with mixed datatypes
my_tuple = ('English', 2, 'Science', 'History', 10)
print(my_tuple) # ('English', 2, 'Science', 'History', 10)

# Nested tuples
my_tuple = ("CompSci", [2, 4, 6], (7, 8, 9))
print(my_tuple) # ('CompSci', [2, 4, 6], (7, 8, 9))

# A tuple can also be created without using parentheses. 
# This is known as tuple packing.

my_tuple = 'Apples', 1.6, 'Corgi'
print(my_tuple) # ('Apples', 1.6, 'Corgi')

# Tuple unpacking is also possible
a, b, c = my_tuple

print(a) # Apples
print(b) # 1.6
print(c) # Corgi

my_tuple = ("Hello World")
print(type(my_tuple))  # <class 'str'>

# Single value needs trailing comma
my_tuple = ("Hello",)
print(type(my_tuple))  # <class 'tuple'>

# Parentheses is optional
my_tuple = "Hello",
print(type(my_tuple))  # <class 'tuple'>

# Indexing

new_tuple = ('A', 'B', 'C', 'D', 'E',) 
print(new_tuple[0]) # A
print(new_tuple[-1]) # E

# Nested tuple

fruits = ('Apples', 'Bananas', 'Coconuts', ['Durians', 'Elderberry'], ('Fuji Apple', 'Grapes', 'Honeyberries'))
print(fruits[3][0]) # Durians
print(fruits[3][1]) # Elderberry
print(fruits[4][-1]) # Honeyberries

# Slicing
fruits2 = fruits

print(fruits2[0:4]) # ('Apples', 'Bananas', 'Coconuts', ['Durians', 'Elderberry'])
print(fruits2[2:]) # ('Coconuts', ['Durians', 'Elderberry'], ('Fuji Apple', 'Grapes', 'Honeyberries'))
print(fruits2[:-1]) # ('Apples', 'Bananas', 'Coconuts', ['Durians', 'Elderberry'])
print(fruits2[:]) # ('Apples', 'Bananas', 'Coconuts', ['Durians', 'Elderberry'], ('Fuji Apple', 'Grapes', 'Honeyberries'))

# Tuples are immutable - unable to change values
first_tuple = (1, 2, 3, 4, 5)
 # first_tuple[0] = 6 # TypeError: 'tuple' object does not support item assignment

# However, item of mutable elements can be changed
second_tuple = (1, 2, 3, 4, [5, 6])
second_tuple[4][1] = 7 # change the 2nd value of [5, 6]
print(second_tuple) # (1, 2, 3, 4, [5, 7])

# Tuples can be reassigned

second_tuple = ['AWS', 'GCP', 'Azure', 'Oracle Cloud']
print(second_tuple) # ['AWS', 'GCP', 'Azure', 'Oracle Cloud']

# Delete tuple
del second_tuple
# print(second_tuple) # NameError: name 'second_tuple' is not defined, second_tuple has been deleted

# Tuple methods - count and index

test_tuple = '1', 1, '2', 2
print(test_tuple.count('1'))
print(test_tuple.index(1))