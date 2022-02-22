# Prob 2
# Create a small program that will:
# Ask for user input
# Count the number of vowels in the user text ('a', 'e', 'i', 'o', 'u', 'y')
# Display the number of vowels in user text

print("Please enter a string")
my_string = input()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
count = 0
for letter in my_string.lower():
    if letter in vowels:
        count += 1
print("Number of vowels in string: " + str(count))

# Prob 3
# Create a small program where
# The user inputs an email
# The program checks if the email ends with @gmail.com
# The program prints True if email ends with @gmail.com and False if it doesn't
print("Please enter a Gmail email")
email = input()
print(email[-10:] == "@gmail.com")