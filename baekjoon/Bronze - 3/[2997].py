a, b, c = sorted(list(map(int, input().split())))

n1, n2 = b-a, c-b
if n1 == n2:
    print(c + n1)
else:
    n = min(n1, n2)
    if n2 != n:
        print(c - n)
    else:
        print(b - n)
