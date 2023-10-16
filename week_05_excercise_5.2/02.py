import random


def beetle_game():
    beetle_parts = {
        6: 'body',
        5: 'head',
        4: 'wing',
        3: 'leg',
        2: 'antenna',
        1: 'eye'
    }

    beetle_dict = {
        'body': 0,
        'head': 0,
        'wing': 0,
        'leg': 0,
        'antenna': 0,
        'eye': 0,
    }
    die_roll_count = 0
    die_roll_freq = []

    game_count = 1

    while game_count <= 100:
        while True:
            die_roll = random.randint(1, 6)

            if beetle_dict['body'] == 1 and beetle_dict['head'] == 1 and beetle_dict['wing'] == 2 and beetle_dict['leg'] == 6 and beetle_dict['antenna'] == 2:
                die_roll_freq.append(die_roll_count)
                beetle_dict = {
                    'body': 0,
                    'head': 0,
                    'wing': 0,
                    'leg': 0,
                    'antenna': 0,
                    'eye': 0,
                }
                die_roll_count = 0
                break

            if die_roll == 6:
                beetle_dict[beetle_parts[die_roll]] = 1

            if die_roll == 5 and beetle_dict['body'] > 0:
                beetle_dict[beetle_parts[die_roll]] = 1

            if die_roll == 4 and beetle_dict['body'] > 0 and beetle_dict['wing'] < 2:
                beetle_dict[beetle_parts[die_roll]] += 1

            if die_roll == 3 and beetle_dict['body'] > 0 and beetle_dict['leg'] < 6:
                beetle_dict[beetle_parts[die_roll]] += 1

            if die_roll == 2 and beetle_dict['head'] > 0 and beetle_dict['antenna'] < 2:
                beetle_dict[beetle_parts[die_roll]] += 1

            if die_roll == 1 and beetle_dict['head'] > 0 and beetle_dict['eye'] < 2:
                beetle_dict[beetle_parts[die_roll]] += 1

            die_roll_count += 1

        game_count += 1

    dice_roll_summ = 0

    for roll in die_roll_freq:
        dice_roll_summ += roll

    avg_dice_roll = dice_roll_summ / len(die_roll_freq)

    print(
        f'The average number of dice roll to win the game is {round(avg_dice_roll)}')


beetle_game()
