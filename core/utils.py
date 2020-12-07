def bhavcopy_date(date):
    day = date.day
    month = date.month
    if 1 <= date.day <= 9:
        day = '0' + str(date.day)
    if 1 <= date.month <= 9:
        month = '0' + str(date.month)

    return str(day) + str(month) + str(date.year)
