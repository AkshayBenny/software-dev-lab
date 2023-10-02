def strToNum(strNum):
    numberDict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    if strNum in numberDict:
        print(numberDict[strNum])
    else:
        print("The key does not exist in the dictionary.")


strToNum("nine")
