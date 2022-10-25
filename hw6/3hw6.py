def read_employees_from_file(path):
    fh = open(path, "r")
    lines = fh.readlines()
    list_lines = [i.strip() for i in lines]
    fh.close()
    return list_lines


print(read_employees_from_file("3hw6.txt"))
