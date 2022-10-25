import re


def find_all_emails(text):
    result = re.findall(
        r"[A-Za-z]{1,}\d{0,}[\.]?\w+[\.]?\w{0,}[@][A-Za-z]+[\.][a-zA-z]{2,}",
        text,
        flags=re.IGNORECASE,
    )
    return result
