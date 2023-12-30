# Add two number
num1 = 15
num2 = 20
sum = num1 + num2
print("Sum of two numbers are ", sum)


# Add two number with user input
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
sum_of_number = float(number1) + float(number2)
print("Sum of two numbers are: ", sum_of_number)


# Add two number using function
def add(a,b):
    return a+b

x = 10
y = 20

sum_of_x_and_y = add(x,y)
print("Sum of two numbers are: ", sum_of_x_and_y)


# Add two number with user input using function
def addNumber(c,d):
    return c+d

X = float(input("Enter the first number: "))
Y = float(input("Enter the second number: "))

sum_of_X_and_Y = addNumber(X,Y)
print("Sum of two numbers are: ", sum_of_X_and_Y)