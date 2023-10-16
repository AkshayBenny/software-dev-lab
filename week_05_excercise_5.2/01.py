my_string = 'Hello world from the University of Strathclyder'


def char_freq_counter(string):
    char_freq_dict = {}
    for char in string.replace(" ", ""):
        if char in char_freq_dict:
            char_freq_dict[char.lower()] += 1
        else:
            char_freq_dict[char.lower()] = 1

    return char_freq_dict


new_char_dict = char_freq_counter(my_string)

print(f'Character counter: {new_char_dict}')


def vowel_freq_counter(string):
    vowel_freq_dict = {}
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in string.replace(" ", ""):
        if (char.lower() in vowels):
            if char in vowel_freq_dict:
                vowel_freq_dict[char.lower()] += 1
            else:
                vowel_freq_dict[char.lower()] = 1
    return vowel_freq_dict


print(f'Vowel counter: {vowel_freq_counter(my_string)}')
