temp = []

for i in range(15):
    temp.append(list(map(str, input().split())))
    
for i in range(15):
    if 'w' in temp[i]:
        print('chunbae')
        break
    elif 'b' in temp[i]:
        print('nabi')
        break
    elif 'g' in temp[i]:
        print('yeongcheol')
        break
