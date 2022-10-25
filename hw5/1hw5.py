def real_len(text):
    signs = ["\n", "\f", "\r", "\t", "\v"]
    new_text = list()
    print(new_text)
    for char in text:
        if char not in signs:
            new_text.append(char)
    print((new_text))
    return text and len(new_text)


text = "Alex\nKdfe23\t\f\v.\r"

print(real_len(text))
