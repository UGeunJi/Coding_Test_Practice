t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    
    if b < 4 or a < 12:
        print(-1)
    else:
        print(11 * b + 4)
