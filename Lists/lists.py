# A list is a collection which is ordered and changeable. 
# Allows duplicate members

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Get a value
print(fruits[1]) # 'Oranges'

# Get length
print(len(fruits)) # 4

# Remove from list
fruits.remove('Oranges')
print(fruits) # ['Apples', 'Grapes', 'Pears']

# Append to list 
fruits.append('Mangos')
print(fruits) # ['Apples', 'Grapes', 'Pears', 'Mangos']

# Insert into position
fruits.insert(0, 'Pineapples')
print(fruits) # ['Pineapples', 'Apple', 'Grapes', 'Pears', 'Mangos']

# Remove with pop using index
fruits.pop(0)
print(fruits) # ['Apples', 'Grapes', 'Pears', 'Mangos']

# Sort the list
fruits.sort()
print(fruits) # ['Apple', 'Grapes', 'Mangos', 'Pears'] 

# Reverse sort
fruits.sort(reverse=True)
print(fruits) # ['Pears', 'Mangos', 'Grapes', 'Apples']

# Reverse the order of list
fruits.reverse()
print(fruits) # ['Apple', 'Grapes', 'Mangos', 'Pears'] 

# Replace value
fruits[0] = 'Durians'
print(fruits) # ['Durians', 'Grapes', 'Mangos', 'Pears']