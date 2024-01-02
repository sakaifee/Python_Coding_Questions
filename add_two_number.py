# Add two numbers
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


# Add two numbers using function with user input 
def addNumber(c,d):
    return c+d
X = float(input("Enter the first number: "))
Y = float(input("Enter the second number: "))
sum_of_X_and_Y = addNumber(X,Y)
print("Sum of two numbers are: ", sum_of_X_and_Y)



# Add two numbers using operator .add() method
first_number = 4
sec_number = 9
import operator
sum_first_sec = operator.add(first_number, sec_number)
print("Sum of two number is: ", (sum_first_sec))



# Add two numbers using operator .add() method with user input
First_Number = float(input("Enter the first number: "))
Second_Number = float(input("Enter the second number: "))
import operator
Sum_Of_Digit = (operator.add(First_Number, Second_Number))
print("Sum of two digit number are: ", Sum_Of_Digit)


# Add two numbers using lambda function
add_number = lambda x, y: x + y
num_1 = 4
num_2 = 5
result = add_number(num_1, num_2)
print("Sum of two digit are: ", result)


# Add two numbers using lambda function with user input
add_number = lambda x, y: x + y
num_1 = 4
num_2 = 6
result = add_number(num_1, num_2)
print("Sum of the two digit number are: ", result)


# Add two numbers using recursive function
def add_number_recursive(x, y):
    if y == 0:
        return x
    else:
        return add_number_recursive(x + 1, y -1)
first_number = 3
sec_number = 4
result = add_number_recursive(first_number, sec_number)
print("Sum of two digit numbers are", result)


# Add two numbers using recursive function with user input
def add_number_recursive(x, y):
    if y == 0:
        return x
    else:
        return add_number_recursive(x + 1, y - 1)
first_number = float(input("Enter the first number: ")) 
sec_number = float(input("Enter the second number: ")) 
result = add_number_recursive(first_number, sec_number)
print("Sum of two numbers are: ", result)
