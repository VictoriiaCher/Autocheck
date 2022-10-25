def write_employees_to_file(employee_list, path):
    fh = open(path, "w")
    new_list = [item for employee in employee_list for item in employee]
    for i in new_list:
        # print(i)
        fh.write(f"{i}\n")
    fh.close()


employee_list = [["Robert Stivenson,28", "Alex Denver,30"], ["Drake Mikelsson,19"]]
path = "2hw6.txt"
write_employees_to_file(employee_list, path)
