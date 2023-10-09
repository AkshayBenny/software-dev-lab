import random


def roll_dice(number_of_dice, number_of_sides):
    sum = 0
    i = 0
    while i < number_of_dice:
        my_rand_value = random.randint(1, number_of_sides)
        sum += my_rand_value
        i += 1

    return sum


roll_my_dice = roll_dice(1, 6)
print(roll_my_dice)
