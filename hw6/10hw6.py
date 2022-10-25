def save_credentials_users(path, users_info):
    with open(path, 'wb') as out:
        for key,value in users_info.items():
            string = f"{key}:{value}\n".encode()
            out.write(string)


path = '10hw6_output.txt'
users_info = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}

save_credentials_users(path, users_info)