def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, "a") as file:
        file.write('\n'+ additional_info)

    with open(path, "r") as file:
        file.seek(start_pos)
        file.read(count_chars)

path='data.txt'
additional_info = 'Hello'
start_pos = 10
count_chars = 5
print(file_operations(path, additional_info, start_pos, count_chars))