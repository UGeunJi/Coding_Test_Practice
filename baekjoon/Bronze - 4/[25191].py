n = int(input())
a, b = map(int, input().split())

sum = a // 2 + b

if sum > n:
    print(n)
else:
    print(sum)
