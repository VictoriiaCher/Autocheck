import base64


def encode_data_to_base64(data):
    base64_list =[]
    for i in data:
        message_bytes = i.encode("utf-8")
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode("utf-8")
        base64_list.append(base64_message)
    return base64_list

data = ['andry:uyro18890D', 'steve:oppjM13LL9e']
print(encode_data_to_base64(data))