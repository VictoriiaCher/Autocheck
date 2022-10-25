import re


def is_spam_words(text, spam_words, space_around=False):
    result = bool(
        re.findall(r"\b{}\b".format(*spam_words), text, flags=re.IGNORECASE)
        if space_around
        else re.findall(r"{}".format(*spam_words), text, flags=re.IGNORECASE)
    )
    return result


print(is_spam_words("Молох бог ужасен.", ["Бог", "лих"], space_around=False))
print(is_spam_words("Ты хорош, но выглядишь как лох.", ["лох"], True))
