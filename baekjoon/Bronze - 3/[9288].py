for i in range(int(input())):
    n = int(input())
    print(f"Case {i + 1}:")
    for a in range(1, 7):
        for b in range(a, 7):
            if a + b == n:
                print(f"({a},{b})")
