a, b = map(int, input().split())
n = int(input())

for i in range(n):
    num = int(input())
    li = list(map(int, input().split()))
    if b in li:
        if i == n - 1:
            print('YES')
        pass
    else:
        print('NO')
        break
