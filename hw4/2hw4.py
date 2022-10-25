def prepare_data(data):
    n = len(data)
    data.sort()
    data.pop(0)
    data.pop(n - 2)
    print(data)
    return data


data = [1, 3.1415, 41, 3]
prepare_data(data)
