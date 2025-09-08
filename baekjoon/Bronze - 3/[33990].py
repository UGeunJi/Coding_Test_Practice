N = int(input())
result = []
 
for _ in range(N):
    A, B, C = map(int, input().split())
    if A + B + C >= 512:
        result.append(A + B + C)
 
if result:
    result.sort()
    print(result[0])
else:
    print(-1)
