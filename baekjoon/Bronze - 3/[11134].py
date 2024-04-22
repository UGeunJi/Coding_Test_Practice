for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a // b + (1 if a % b else 0))
