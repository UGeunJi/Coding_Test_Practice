N, X = map(int, input().split())
T = list(map(int, input().split()))
check = True

while check:
    for i in range(N):
        if X <= T[i]:
            X += 1
        else:
            result = i
            check = False
            break

print(result+1)
