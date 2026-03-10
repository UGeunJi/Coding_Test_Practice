n = int(input())
temp = []

for i in range(n):
    t_s = 0
    t = int(input())
    
    for j in range(t):
        s, num, p = map(str, input().split())
        t_s += float(num) * float(p)
    
    temp.append(t_s)

for k in range(len(temp)):
    print('$%.2f'%(temp[k]))
