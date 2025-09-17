for a in range(int(input())):
    if a != 0:
        print()
    n = int(input())
    s = 0
    for i in range(1, n):
        if n%i == 0:
            s += i
    if s == n:
        print("%d is a perfect number." % (n))
    elif s < n:
        print("%d is a deficient number." % (n))
    else:
        print("%d is an abundant number." % (n))
