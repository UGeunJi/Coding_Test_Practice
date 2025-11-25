while True:
    year = int(input())

    if year == 0:
        break

    if 1896 <= year and year % 4 == 0:
        if 1914 <= year <= 1918 or 1939 <= year <= 1945:
            print(year, "Games cancelled")
        elif 2020 < year:
            print(year, "No city yet chosen")
        else:
            print(year, "Summer Olympics")
    else:
        print(year, "No summer games")
