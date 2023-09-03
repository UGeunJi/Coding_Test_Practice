s = input()

cnt = 0
ub = 0

cnt += len(s)

for i in s:
    if i == ':':
        cnt += 1
    if i == '_':
        ub += 1
        
print(cnt + (ub * 5))
