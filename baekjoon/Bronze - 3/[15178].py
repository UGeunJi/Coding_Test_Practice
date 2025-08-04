for _ in range(int(input())):
    li = list(map(int, input().split()))
    print(*li, end=' ')
    print("Seems OK" if sum(li) == 180 else "Check")
