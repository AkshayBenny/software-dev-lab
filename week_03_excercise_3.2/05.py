def strToInt(strNum):
    try:
        print(int(strNum) + 10)
    except ValueError as e:
        print(f"Error {e} {e.__class__.__name__}")


strToInt("4asdsd")
