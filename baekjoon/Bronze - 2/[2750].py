n = int(input())
li = []
for i in range(n):
    li.append(int(input()))
    li.sort()

for i in range(len(li)):
    print(li[i])
