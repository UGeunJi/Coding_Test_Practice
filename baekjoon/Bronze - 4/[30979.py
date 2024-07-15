n = int(input())
a = int(input())
li = list(map(int, input().split()))
s = sum(li)

if s >= n:
    print('Padaeng_i Happy')
else:
    print('Padaeng_i Cry')
