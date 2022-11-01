from datetime import date


def get_days_in_month(month, year):
    data = date(year=year, month=month, day=1)
    future_data = (
        date(year=year, month=month + 1, day=1)
        if month != 12
        else date(year=year + 1, month=1, day=1)
    )
    dif = future_data - data
    return dif.days


print(get_days_in_month(3, 2021))
