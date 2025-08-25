while 1:
    sp, w, st = map(float, input().split())
    p = 0
    if sp == w == st == 0:
        break
    if sp <= 4.5 and w >= 150 and st >= 200:
        p = 1; print("Wide Receiver", end = ' ')
    if sp <= 6.0 and w >= 300 and st >= 500:
        p = 1; print("Lineman", end = ' ')
    if sp <= 5.0 and w >= 200 and st >= 300:
        p = 1; print("Quarterback", end = ' ')
    if p == 0:
        print("No positions", end = ' ')
    print()
