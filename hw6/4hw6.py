def add_employee_to_file(record, path):
    fh = open(path, "a")
    fh.write(record + "\n")
    fh.close()


record = "Drake Mikelsson,19"
path = "4hw6.txt"

add_employee_to_file(record, path)
