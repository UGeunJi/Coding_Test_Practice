while 1:
    a, b = input().split()
    if a == b == '0':
        break
    if len(a) > len(b):
        b = (len(a) - len(b)) * '0' + b
    else:
        a = (len(b) - len(a)) * '0' + a
    c = cc = 0
    for i in range(len(a) - 1, -1, -1):
        if int(a[i]) + int(b[i]) + cc >= 10:
            c += 1
            cc = 1
        else:
            cc = 0
    print(c)
