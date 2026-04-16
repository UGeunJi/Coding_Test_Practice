n = int(input())
li = list(map(int, input().split()))
temp = []
cnt = 0

for i in range(len(li)):
    if li[i] in temp:
        cnt += 1
    temp.append(li[i])
    
print(cnt)
