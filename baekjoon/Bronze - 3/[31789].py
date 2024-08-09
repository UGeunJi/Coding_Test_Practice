n = int(input())
a, b = map(int, input().split())
w = [list(map(int, input().split())) for _ in range(n)]

result = False

for c, p in w:
    if c <= a and p > b:
        result = True
        break

if result:
    print("YES")
else:
    print("NO")
