import math

n = int(input())

for _ in range(n):
    l = list(map(int, input().split()))
    sum = 0
    f = l.pop(0)
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            sum += math.gcd(l[i], l[j])
    
    print(sum)
