def get_credentials_users(path):
    with open(path, 'rb') as s:
        return [line.strip().decode() for line in s.readlines()]

print(get_credentials_users('10hw6_output.txt'))