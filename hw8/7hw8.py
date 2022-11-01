import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    result_list = []
    if isinstance(cats[0], dict):
        for i in cats:
            result_list.append(Cat._make(i.values()))
    else:
        for i in cats:
            result_list.append(i._asdict())
    return result_list


cats_tuple = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
print(convert_list(cats_tuple))

cats_tuple2 = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]
print(convert_list(cats_tuple2))
