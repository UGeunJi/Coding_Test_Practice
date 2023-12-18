n = int(input())
cnt = 0

for i in range(n):
    s = input()
    if s.count('01') >= 1 or s.count('OI'):
        cnt += 1
        
print(cnt)
