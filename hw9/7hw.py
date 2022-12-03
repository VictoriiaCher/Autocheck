def normal_name(list_name):
    name = []
    for i in map(lambda x: x.title(), list_name):
        name.append(i)
    return name


list_name = ["dan", "jane", "steve", "mike"]
print(normal_name(list_name))
