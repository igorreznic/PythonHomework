# Ex2.
#
# Ask the user to input a number n. Following that, for n times:
# Ask the user to input a number and add the number to the list.
# After the user has input all the numbers, calculate the average value of the numbers in the list and print it

n = int(input('Input a number: '))
the_list = []
sum = 0
for i in range(n):
    number = int(input('Enter a number: '))
    the_list.append(number)
    sum += number
print(f'The average value is {sum/len(the_list)}')


