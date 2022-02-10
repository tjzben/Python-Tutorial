# Strings in Python are surrounded by either single, double or triple quotation marks for multi lines .

first_name = 'Ben'
last_name = "Tan"
profile = """Getting started with 
Learning Python
"""
age = 34

print(profile)

# Concatenate 
print("Hello, my name is " + first_name + " and I am " + str(age))

# User input

my_name = input('What is your name: ')
print(my_name) # What is your name: 

# F-Strings

weight = 70
height = 1.76
print(f"I weight {weight} KG and my height is {height} CM")

# String methods

x = "hello World"

# Upper case
print(x.upper())

# Lower case
print(x.lower())

# Capitalize the first word of 'hello world'
print(x.capitalize()) 

# Find position of alphabet 'W'
print(x.find('W'))

# Replace words in string
print(x.replace("hello", "hi"))

# Split the string
print('My Python Learning Journey'.split())

# Join the string
print(' '.join(['Liverpool', 'Football', 'Club']))

# Print len of string
b = "Liverpool Football Club"
print(len(b))

# Indexing and Slicing

y = "Peter's youngester son is 2 years old"
print(y[0])
print(y[0:5])
print(y[-2])
print(y[-1:-5])

# Whitespace characters in string

# Newline \n
# Space \s
# Tab \t

z = ('This is lazy \n\t')
print(z.split())
print(z.strip())