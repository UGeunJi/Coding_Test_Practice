ds, ys = map(int, input().split())
dm, ym = map(int, input().split())
sun_year = ys - ds
moon_year = ym - dm

while sun_year != moon_year :
    if sun_year < moon_year :
        sun_year += ys
    else : moon_year += ym
print(sun_year)
