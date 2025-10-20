a, b, c = map(int, input().split())
t = int(input())
money = 0

if t <= 30:
    print(a)
else:
    if (t - 30) % b == 0:
        money = a + (((t - 30) // b) * c)
    else:
        money = a + (((((t - 30) // b) + 1) * c))

    print(money)
