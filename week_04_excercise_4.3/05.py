def update_dict(d):
    d.clear()
    d["a"] = 1
    d["b"] = 2

    return d


d2 = {}
print(update_dict(d2))
