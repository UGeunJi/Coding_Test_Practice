a, b = map(int, input().split())
x, y = map(int, input().split())

cnt = 0

for i in range(x - y, x + y + 1):
    if i >= a and b >= i:
        cnt += 1
        
if cnt == 0:
    print('IMPOSSIBLE')
else:
    print(cnt)
