# Ex3.
#
# We are going to create a program where we find find the person with the highest score.
#
# Ask the user to input a number n. Following that, for n times:
# Ask the user to input a name (name of the person), and add it to a list
# Ask the user to input a number (the score of the person) and add it to another list
# After the user has input all values, find the highest score in the list, and print the name of the person with the highest score.

n = int(input('Input a number: '))
names_list = []
scores_list = []
max_score = 0

for i in range(n):
    name = input('Enter a name: ')
    score = int(input('Enter a score: '))
    names_list.append(name)
    scores_list.append(score)
    if score > max_score:
        max_score = score
        index = i

print(f'{names_list[index]} are cel mai mare scor')
#print(f'{names_list[scores_list.index(max(scores_list))]} are cel mai mare scor')