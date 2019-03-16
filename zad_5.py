
def isomorphic(word_1, word_2):
    dict_1 = {}
    if len(word_1) == len(word_2):
        for letter in zip(word_1, word_2):
            if dict_1.setdefault(letter[1], letter[0]) != letter[0]:
                return False
    return True


print(isomorphic('fro', 'add'))
