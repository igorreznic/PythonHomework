
def is_palindrom(given_word):
    word = given_word.lower().replace(' ', '')
    for i in range(len(word)//2):
        if not word[i] == word[-i-1]:
            return False
    return True

