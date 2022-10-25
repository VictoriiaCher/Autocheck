def is_check_name(fullname, first_name):
    return True if fullname.find(first_name) > -1 else False


print(is_check_name("Alex Old", "Alex"))
