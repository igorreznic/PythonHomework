from Ex1 import is_palindrom
from Ex2 import is_prime
from Ex3 import perfect_numbers

print("Which exercise would you like to test? \n "
      "1: To check if a string is a Palindrome \n "
      "2: To check if a number is prime \n "
      "3: To find a perfect number \n "
      "4: To...")

exercise_number = input('Enter a number: ')

if exercise_number == '1':
    my_string = input('Enter a word or a phrase:')
    if is_palindrom(my_string):
        print(f'{my_string} is a palindrome')
    else:
        print(f'{my_string} is not a palindrome')

if exercise_number == '2':
    number = int(input('Enter a number: '))
    if is_prime(number):
        print(f'{number} is a prime number')
    else:
        print(f'{number} is not a prime number')

if exercise_number == '3':
    number = int(input('Enter a number: '))
    print(f'These are the first {number} perfect numbers: {perfect_numbers(number)}')