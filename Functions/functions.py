# Create a simple function to print name
def sayHello(name):
    print(f"Hi, {name}")

# Call function sayHello() and passing in the parameter
sayHello('Ben') # Hi, Ben

# Return value
def getSum(num1, num2, num3):
    total = num1 + num2 * num3
    return total

print(getSum(1, 5, 7)) # 36

# Function - Area of Triangle
def areaOfTriangle(x, y):
    area = (x * y) / 2
    return area

# User input
length_of_base = int(input("Length of Base: "))
length_of_height = int(input("Length of Height: "))

print(areaOfTriangle(length_of_base, length_of_height)) # 50

# Lambda Function

getTotal= lambda num1, num2: num1 + num2

print(getTotal(1,2)) # 3