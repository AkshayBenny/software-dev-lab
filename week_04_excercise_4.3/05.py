def update_dict(d):
    d.clear()

    d["red"] = 1
    d["blue"] = 2

    return d


d2 = {}
print(update_dict(d2))
