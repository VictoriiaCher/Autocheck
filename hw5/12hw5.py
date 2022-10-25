import re


def replace_spam_words(text, spam_words):
    for word in spam_words:
        text = re.sub(word, "*" * len(word), text, flags=re.IGNORECASE)
    return text


text = """Guido van Rossum began working on Python in the late 1980s, as a"""
spam_words = ["began", "Python"]

print(replace_spam_words(text, spam_words))
