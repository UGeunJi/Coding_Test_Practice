n = int(input())

for i in range(n):
    l1 = [0]
    l2 = list(input())
    for i in range(len(l2)):
        if l2[i] == l1[-1]:
            pass
        else:
            l1.append(l2[i])
            
    l1.pop(0)    
    print(''.join(l1))
