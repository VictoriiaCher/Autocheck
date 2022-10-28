import re


def token_parser(s):
    token_list = re.findall(r"\d+|[+]|-|\*|\/|\)|\(", s)
    return token_list


print(token_parser("2+ 34-5 * 3"))
print(token_parser("2+ 34-5 * (2+3)"))
