# Ex4.
#
# Create a program that is going to take a whole number as an input, and will calculate the factorial of the number.
#
# Factorial example: 5! = 5 * 4 * 3 * 2 * 1 = 120

factorial = 1
number = int(input('Enter a number: '))
for i in range(1, number+1):
    factorial *= i
print(f'Factorial of {number} is {factorial}')