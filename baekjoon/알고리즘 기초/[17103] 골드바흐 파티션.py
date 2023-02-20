import sys

prime = [True for i in range(1000001)]

prime[0] = prime[1] = False
for i in range(2, 1001):
    if prime[i]:
        for j in range(i + i, 1000001, i):
            prime[j] = False

n = int(sys.stdin.readline())

for i in range(n):
    answer = 0
    num = int(sys.stdin.readline())

    for i in range(2, num // 2 + 1):
        if prime[i] and prime[num - i]:
            answer += 1
    print(answer)
