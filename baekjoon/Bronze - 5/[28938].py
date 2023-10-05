n = int(input())
l = list(map(int, input().split()))
s = 0

for i in range(len(l)):
    s += l[i]
    
if s < 0:
    print('Left')
elif s == 0:
    print('Stay')
else:
    print('Right')
