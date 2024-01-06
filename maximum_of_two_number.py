# Maximum of two numbers in python
def maximum_number(num1, num2):
    if(num1 >= num2):
        return num1
    else:
        return num2
num1 = 3
num2 = 14

print(maximum_number(num1, num2))


# Maximum of two number using ternary operator
first_number = 23
sec_number = 32
print(first_number if first_number >= sec_number else sec_number)


# Maximum of two number using max() function
a = 3
b = 4
maximum = max(a,b)
print(maximum)


# Maximum of two number using max() function with user input
a1 = input("Enter the first number: ")
b1 = input("Enter the second number: ")
max_num = max(a1,b1)
print("The maximum number of these two are: ", max_num)


# Maximum of two number using lamda function
num1 = 2
num2 = 3
maximum_num = lambda num1,num2:num1 if num1 > num2 else num2
print("The maximum of these two numbers are: ", maximum_num(num1,num2))