import re


def find_all_links(text):
    result = []
    iterator = re.finditer(
        r"([h]{1}[t]{2}[p]{1}[s]?[:][/]{2}[w]{3}[\.]|[h]{1}[t]{2}[p]{1}[s]?[:][/]{2})[a-z]\w+[\.][a-z]{3}",
        text,
    )
    for match in iterator:
        result.append(match.group())
    return result


text = "The main search site in the world is https://www.google.com The main social network for people in the world is https://www.facebook.com But programmers have their own social network http://github.com There they share their code. some url to check https://www..facebook.com www.facebook.com"
print(find_all_links(text))
