n = int(input())

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if l2[i] >= l1[i]:
        cnt += 1
        
print(cnt)
