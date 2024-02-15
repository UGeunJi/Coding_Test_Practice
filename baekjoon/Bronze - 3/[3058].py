n = int(input())

for _ in range(n):
    li = list(map(int, input().split()))
    temp = 0
    temp_li = []
    for i in range(len(li)):
        if li[i] % 2 == 0:
            temp += li[i]
            temp_li.append(li[i])
                
    print(f'{temp} {min(temp_li)}')
