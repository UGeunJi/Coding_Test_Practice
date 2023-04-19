n = input()

if len(n) == 2:
    print(sum(map(int, [n[0], n[1]])))
elif len(n) == 4:
    print(20)
else:
    if int(n[-1]) == 0:
        print(int(n[0]) + 10)
    else:
        print(int(n[-1]) + 10)
