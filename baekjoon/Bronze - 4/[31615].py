a = int(input())
b = int(input())

if ((a + b) // 10) < 1:
    print(1)
elif ((a + b) // 100) >= 1:
    print(3)
else:
    print(2)
