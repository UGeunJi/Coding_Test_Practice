lv, t = map(str, input().split())

if t == 'miss':
    print(0)
elif t == 'bad':
    print(200 * int(lv))
elif t == 'cool':
    print(400 * int(lv))
elif t == 'great':
    print(600 * int(lv))
elif t == 'perfect':
    print(1000 * int(lv))
