from datetime import datetime


def get_days_from_today(date):
    list_date = date.split("-")
    date = datetime(
        year=int(list_date[0]), month=int(list_date[1]), day=int(list_date[2])
    ).date()
    today = datetime.now().date()
    return (today - date).days


date = "2021-10-09"
print(get_days_from_today(date))
