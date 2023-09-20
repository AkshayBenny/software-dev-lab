myDictionary = {
    'list01': [1, 2, 3, 4, 5],
    'list02': [6, 7, 8, 9]
}

for key, value in myDictionary.items():
    # print('key:', key, 'value:', value)

    if type(value) == list:
        for i in value:
            print(i)
