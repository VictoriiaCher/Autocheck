articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(string, letter_case=False):
    new_articles_dict = []
    for dict in articles_dict:
        if letter_case:  # учитывает регистр
            if str(dict).find(string) != -1:
                new_articles_dict.append(dict)
        else:
            low_dict = str(dict).lower()
            if low_dict.find(string.lower()) != -1:
                new_articles_dict.append(dict)
    return new_articles_dict


print(find_articles("Ocean", letter_case=True))
