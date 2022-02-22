
def text_info(text: str):
    words_set = set()
    punctuation_list = []
    punctuation_set = set()
    for i in text:
        if not i.isalnum() and i != " ":
            punctuation_list.append(i)
    punctuation_set.update(punctuation_list)

    for punctuation in punctuation_set:
        text = text.replace(punctuation, "")

    words_list = text.split(" ")
    words_set.update(words_list)

    print(f'Words used in text: {words_set}')
    print(f'Punctuation marks used in text: {punctuation_set}')
    print(f'Most used word in text is: {get_most_used(words_list)}')
    print(f'Most used punctuation in text is: {get_most_used(punctuation_list)}')



def get_most_used(the_list: list):
    most_used = None
    times_count = 0
    for item in the_list:
        if the_list.count(item) > times_count:
            times_count = the_list.count(item)
            most_used = item

    return most_used
