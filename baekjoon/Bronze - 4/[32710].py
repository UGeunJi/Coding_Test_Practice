n = int(input())
check = False

for i in range(2, 10):
    if not check:
        for j in range(1, 10):
            table = [i, j, i * j]
            if n in table:
                check = True
                break
    else:
        break

if check:
    print(1)
else:
    print(0)
