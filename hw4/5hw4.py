def lookup_key(data, value):
    list_keys = []
    for d, val in data.items():
        if value == val:
            list_keys.append(d)
    return list_keys


k = lookup_key({"key1": 1, "key2": 2, "key3": 3, "key4": 2}, 2)
print(k)
