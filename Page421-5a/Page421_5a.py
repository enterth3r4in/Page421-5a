#Variable method program that performs an operation on 2 numeric variables.
import os
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
    print("Let's start simple here.")
    print("The sum of the numbers you entered is: ", total, "\n")

def difference(number1, number2):
    print("Negatives can be fun! No reason to do any error checking or fancy if/elses here")
    total = number1 - number2
    print("The difference of the numbers you entered is: ", total, "\n")

def quotient(number1, number2):
    if(number2 == 0):
        print("You broke the world. Good job.")
        input("Press enter to step inside the black hole you've created.\n")
    elif(int(total) == 0):
        print(number2, " can't go into ", number1, " evenly at all. Sorry about that...")
        input("Press enter to accept this sad reality and move on.\n")
    else:
        total = number1 / number2
        print("The quotient of the numbers you entered is: ", int(total), "\n")

def product(number1, number2):
    total = number1 * number2
    return total


calcAgain = ""

print("Welcome to the useless math program!\n")

while calcAgain != "quit":
    num1 = int(input("Please enter a numeric value: "))
    num2 = int(input("Please enter another numeric value: "))
    print("")

    sum(num1, num2)
    difference(num1, num2)
    quotient(num1, num2)
    
    print("Here is something you didn't ask for! It's even outside a method!")
    print("The product of the numbers you entered is: ", product(num1, num2), "\n\n")

    calcAgain = input("Press enter to calculate again or 'quit' to end: ")

os.system('cls')
print("\nThank you for using the useless math program!\n\n")
print("The reason the product is outside the method and not the")
print("quotient function is because of all the fancy code inside")
print("the quotient method. By fancy I mean not fancy.")
input("Press enter to give me full credit even though I didn't follow directions")
os.system('cls')
print("Thanks\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") #This seems ugly and ineffecient. Gotta be a way to put a line at the very end of the console or something.