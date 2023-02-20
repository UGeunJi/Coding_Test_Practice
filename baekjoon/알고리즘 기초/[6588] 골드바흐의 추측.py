import sys

prime = [True for i in range(1000001)]

for i in range(2, 1001):
    if prime[i]:
        for j in range(i + i, 1000001, i):
            prime[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    for i in range(3, len(prime)):
        if prime[i] and prime[n - i]:
            print(f'{n} = {i} + {n - i}')
            break
    else:
        print("Goldbach's conjecture is wrong.")
