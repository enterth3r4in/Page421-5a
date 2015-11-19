#Variable method program that performs an operation on 2 numeric variables.

'''
Would require 2 user inputted variables.
num1, num2

sum is num1 + num2
diff is num1 - num2
quotient is num1 / num2
product is num1 * num2

Each method responsible for outputting it's own answer with information.
'''

def sum(number1, number2):
    total = number1 + number2
    print("The sum of the numbers you entered is: \n", total)

def difference(number1, number2):
    total = number1 - number2
    print("The difference of the numbers you entered is: \n", total)

def quotient(number1, number2):
    total = number1 / number2
    print("The quotient of the numbers you entered is: \n", int(total))

def product(number1, number2):
    total = number1 * number2
    print("The product of the numbers you entered is: \n", total)

print("Welcome to the useless math program!\n")
num1 = int(input("Please enter a numeric value: "))
num2 = int(input("Please enter another numeric value: "))

sum(num1, num2)
difference(num1, num2)
quotient(num1, num2)
product(num1, num2)

print("Thank you for using the useless math program!\n\n")