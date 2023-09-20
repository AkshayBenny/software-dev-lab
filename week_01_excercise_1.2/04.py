authors = {
    'John Doe': 4,
    'Jane Doe': 6,
    'Alex': 6,
    'Benny': 6,
}

num = 0

for key, value in authors.items():
    if (num < 2):
        print(key, value)
    num += 1
