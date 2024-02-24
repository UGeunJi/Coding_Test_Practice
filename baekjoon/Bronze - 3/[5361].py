n = int(input())

for i in range(n):
    sum = 0
    li = list(map(int, input().split()))
    sum = li[0] * 350.34 + li[1] * 230.90 + li[2] * 190.55 + li[3] * 125.30 + li[4] * 180.90
    print(f'${sum:.2f}')
