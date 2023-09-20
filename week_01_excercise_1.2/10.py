myList = [[1, 2, 3, 4], [5, 6, 7, 8]]

for item in myList:
    if type(item) == list:
        for i in item:
            print(i)
    else:
        print(item)
