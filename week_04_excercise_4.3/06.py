
dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}


def mapper(text, my_dict):

    mapped_text = ''

    for letter in text:
        if letter in my_dict:
            if mapped_text == '':
                mapped_text += str(my_dict[letter])
            else:
                mapped_text = mapped_text + ' ' + \
                    '|' + ' ' + str(my_dict[letter])

    return mapped_text


print('>>>', mapper("abc", dict))
