
def string_eliminate_punctuation(text: str):
    punctuation_marks = [".", ",", "!", "?", "-", ";", ":", "'", "(", ")", "[", "]"]
    for punctuation_mark in punctuation_marks:
        text.replace(punctuation_mark, "")
    return text


print(string_eliminate_punctuation("acum, ai spus# ca nu vii?"))