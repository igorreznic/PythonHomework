# Ex1. Having a list Ex: [32, 19, 39, 30]
#
# Write a program that will calculate and:
#
# Print the length of the list
# Print the sum of the numbers in the list
# Print the numbers from the list that are even

my_list = [13, 42, 67, 38, 83, 12]
sum = 0
even_numbers =[]

for element in my_list:
    sum += element
    if element % 2 == 0:
        even_numbers.append(element)
print(f'The length of the list is {len(my_list)}')
print(f'The sum of the numbers is {sum}')
print(f'Even numbers are {even_numbers}')