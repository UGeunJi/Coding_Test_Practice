l = []

for _ in range(4):
    l.append(int(input()))
    
if (l[0] == 8 or l[0] == 9) and (l[-1] == 8 or l[-1] == 9) and (l[1] == l[2]):
    print('ignore')
else:
    print('answer')
