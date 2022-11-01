from datetime import datetime
import re


def get_str_date(date):
    list_date = re.split("-|:|\.| ", date)
    y, m, d = list_date[0:3]
    desired_date = datetime(year=int(y), month=int(m), day=int(d))
    return desired_date.strftime("%A %d %B %Y")


date = "2021-05-27 17:08:34.149Z"

print(get_str_date(date))
