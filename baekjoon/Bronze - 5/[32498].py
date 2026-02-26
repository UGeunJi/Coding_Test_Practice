n = int(input())
cnt = 0

for i in range(n):
    s = int(input())
    if s % 2 != 0:
        cnt += 1
        
print(cnt)
