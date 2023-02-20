import math

n = int(input())

for i in range(n):
    A, B = map(int, input().split())
    GCD = math.gcd(A, B)
    answer = A * B / GCD 
    print(int(answer))
