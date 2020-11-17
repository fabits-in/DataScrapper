def csvA(name=f"raw/2002:02:11.csv"):
    f = open(name, 'r')
    lines = f.read().split("\n")
    dict = {}
    for i in range(len(lines)):
        if i == 0:
            continue
        else:
            elem = lines[i].split(",")
            for x in range(len(elem)):
                if x == 1:
                    dict[elem[x]] = int(elem[x + 2])
    return str(dict)


def csvB(name=f"raw/2002:02:12.csv"):
    f = open(name, 'r')
    lines = f.read().split("\n")
    dict = {}
    for i in range(len(lines)):
        elem = lines[i].split(",")
        if elem[0] == "Record Type":
            m = i
    for i in range(len(lines)):
        for x in range(m + 1, len(lines) - 1):
            ele = lines[x].split(",")
            for y in range(len(ele)):
                if y == 2:
                    dict[ele[y]] = int(ele[y + 3])
        break
    f.close()
    return str(dict)

def parseJson():
    from datetime import date, timedelta

    sdate = date(2002, 1, 1)  # start date
    edate = date(2020, 11, 14)  # end date
    date_modified = sdate
    list = [sdate]
    while date_modified < edate:
        date_modified += timedelta(days=1)
        list.append(date_modified)
    for date in list:
        day = date.day
        month = date.month
        if 1 <= date.day <= 9:
            day = '0' + str(date.day)
        if 1 <= date.month <= 9:
            month = '0' + str(date.month)

        import os.path
        name = f"raw/{date.year}:{month}:{day}.csv"
        if os.path.isfile(name):
            try:
                if date.year == 2002 and (month == str('01') or (month == str('02') and day <= int('11'))):
                    print(csvA(name))
                    # f = open(f"parsedRaw/{date.year}:{month}:{day}.json", 'w')
                    # f.write(csvA(name))
                    # f.close()
                else:
                    print(csvB(name))
                    # f = open(f"parsedRaw/{date.year}:{month}:{day}.json", 'w')
                    # f.write(csvB(name))
                    # f.close()

            except:
                pass


parseJson()