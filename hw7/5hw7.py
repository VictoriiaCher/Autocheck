import re


def capital_text(s):
    list_sentence = []
    sign = re.findall(r"\. |! |\? ", s)
    string = re.split(r"\. |! |\? ", s)
    for sentence in string:
        sentence = sentence[0].upper() + sentence[1:]
        list_sentence.append(sentence)

    for i, v in enumerate(sign):
        list_sentence.insert(2 * i + 1, v)

    return "".join(list_sentence)


print(capital_text("привет вика. сегодня! да"))
print(capital_text("как дела. босс? ay"))
