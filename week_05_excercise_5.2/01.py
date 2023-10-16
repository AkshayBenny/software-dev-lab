my_string = 'Hello world from the University of Strathclyder'


def char_freq_counter(string):
    char_dict = {}
    for char in string.replace(" ", ""):
        if char in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1

    return char_dict


new_char_dict = char_freq_counter(my_string)

print(f'{new_char_dict}')
