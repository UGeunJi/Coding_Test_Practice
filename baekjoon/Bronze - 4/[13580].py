l = sorted(list(map(int, input().split())))

if l[0] == l[1]:
    print("S")
elif l[1] == l[2]:
    print("S")
elif l[0] + l[1] == l[2]:
    print("S")
else:
    print('N')
