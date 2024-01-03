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