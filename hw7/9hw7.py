def all_sub_lists(data):
    n = len(data)
    sub_list = [[]]
    for i in range(n+1):
        for j in range(i+1, n+1):
            sub_list.append(data[i: j])
    sub_list.sort(key=len)
    return sub_list

print(all_sub_lists([1, 1, 3, 6,5]))
