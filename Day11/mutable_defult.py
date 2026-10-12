def wrong_add(item, items=[]):
    items.append(item)
    return items


print(wrong_add("Apple"))
print(wrong_add("Banana"))


def correct_add(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items


print(correct_add("Apple"))
print(correct_add("Banana"))