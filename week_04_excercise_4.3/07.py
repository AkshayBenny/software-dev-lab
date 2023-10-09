
dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}


def get_corresponding_key(val, my_dict):
    for key, value in my_dict.items():
        if int(val) == int(value):
            return key

    return


def reverse_mapper(text, my_dict):
    my_nums = text.split("|")
    mapped_number = ''
    for number in my_nums:
        mapped_number += str(get_corresponding_key(number, my_dict))
    return mapped_number


print(reverse_mapper("1|2|3", dict))
