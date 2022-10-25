import re


def total_salary(path):
    fh = open(path, "r")
    lines = fh.readlines()
    list_salary = []

    for note in lines:
        salary = re.findall(r"\d+", note)
        list_salary.extend(salary)

    fh.close()
    return sum(float(i) for i in list_salary)


print(total_salary("1hw6.txt"))
