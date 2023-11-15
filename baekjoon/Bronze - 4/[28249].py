n = int(input())
sum = 0

for i in range(n):
    s = input()
    if s == 'Poblano':
        sum += 1500
    elif s == 'Mirasol':
        sum += 6000
    elif s == 'Serrano':
        sum += 15500
    elif s == 'Cayenne':
        sum += 40000
    elif s == 'Thai':
        sum += 75000
    else:
        sum += 125000
    
print(sum)
