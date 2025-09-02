for _ in range(int(input())):
    x, k, h = map(int, input().split())
    total = h * 2 * x
    k = k - h

    if k > 140:
        total += (140 * x) + int((k - 140) * 1.5 * x)
    else:
        total += k * x

    print(f"{total:,}")
