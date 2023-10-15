a, b = map(int, input().split())

for i in range(a):
    num = list(input())[::-1]
    print(''.join(num))
