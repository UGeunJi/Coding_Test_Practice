for i in range(int(input())):
    print(f"Case {i + 1}:")
    for _ in range(int(input())):
        n = int(input())
        if n > 5:
            continue
        print(n + 1)
