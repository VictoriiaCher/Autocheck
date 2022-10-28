def data_preparation(list_data):
    new_list = []
    for data in list_data:
        if len(data) > 2:
            data.sort()
            data.pop(0)
            data.pop(len(data) - 1)
        new_list.extend(data)
    new_list.sort(reverse=True)
    return new_list


print(data_preparation([[1, 2, 3], [3, 4], [6, 5]]))
