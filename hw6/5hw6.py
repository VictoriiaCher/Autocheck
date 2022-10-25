def get_cats_info(path):
    with open(path, "r") as fh:
        new_lines = []
        keys = ["id", "name", "age"]
        lines = [line.strip().split(",") for line in fh.readlines()]
        for i in range(len(lines)):
            dictionary = dict(zip(keys, lines[i]))
            new_lines.append(dictionary)
    return new_lines


print(get_cats_info("5hw6.txt"))
