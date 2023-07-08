D = 0
P = 0
n = int(input())

for i in range(n):
    s = input()
    if s == 'D':
        D += 1
    else:
        P += 1
    
    if abs(D - P) >= 2:
        break
        
print(f'{D}:{P}')
