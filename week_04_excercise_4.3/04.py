import random


def give_me_my_future():
    my_future_list = ["You will die tomorrow", "bleh", "blue", "green"]

    my_rand_index = random.randint(0, len(my_future_list)-1)

    return my_future_list[my_rand_index]


print(give_me_my_future())
