points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    point = coordinates
    sum = 0
    for i in range(len(point) - 1):
        if point[i] > point[i + 1]:
            tup = (point[i + 1], point[i])
        else:
            tup = (point[i], point[i + 1])
        sum += points[tup]
    return sum if len(point) > 1 else 0


print(calculate_distance([0, 1, 3, 2, 0, 2]))
