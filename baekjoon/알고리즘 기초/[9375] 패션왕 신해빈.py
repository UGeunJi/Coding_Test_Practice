t = int(input())

for _ in range(t):
    kind = []

    for _ in range(int(input())):
        kind.append(input().split()[1])
    
    cnt = 1

    for i in set(kind):
        cnt *= kind.count(i) + 1
    
    print(cnt - 1)
