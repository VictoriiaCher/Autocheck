def split_list(grade):
    if grade == []:
        return ([], [])
    else:
        mid = sum(grade) / len(grade)
        first = []
        second = []

        for i in grade:
            if i <= mid:
                first.append(i)
            else:
                second.append(i)
        return (first, second)


print(split_list([1, 12, 3, 24, 5]))
