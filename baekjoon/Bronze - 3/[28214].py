N, K, P = map(int, input().split())
B = list(map(int, input().split()))
available = 0

for i in range(N):
    count = 0
    for j in range(K):
        if B[i*K+j] == 0:
            count += 1
    if count < P:
        available += 1

print(available)
