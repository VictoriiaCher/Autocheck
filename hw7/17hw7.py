def encode(data):
    if not data:
        return []
    index = 1
    while index < len(data) and data[index] == data[index - 1]:
        index = index + 1
    return [data[0], index] + encode(data[index:])


data = ['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z']

print(encode(data))
