a = int(input())

if (a * 0.01 + 25) < 100:
    print(100)
elif (a * 0.01 + 25) > 2000:
    print(2000)
else:
    print(a * 0.01 + 25)
