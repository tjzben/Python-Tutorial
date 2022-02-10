import constant

# Variables assignment
a = 2 # int
b = 2.5 # float
first_name = 'Ben' # string
is_cold = True # boolean 

# Multiple assignment
x, y, name, is_hot = (1, 2.5, 'Ben', True)
print(x) # 1
print(y) # 2.5
print(name) # Ben
print(is_hot) # True
print(type(x)) # <class 'int'>

# Assign same value to multiple variables 
x = y = z = "same"
print(x) # same
print(y) # same
print(z) # same

# Casting
a = 10.5
print(int(a)) # 10 

# Import constant values
print(constant.PI) # 3.142
print(constant.GRAVITY) # 9.8



