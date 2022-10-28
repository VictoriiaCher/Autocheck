def decode(data):
    if not data:
        return []
    else:
        return [i for d in [data[0] * data[1]] for i in d] + [i for d in decode(data[2:]) for i in d]


data = ['X', 3, 'Y', 1, 'Z', 2]
print(decode(data))

