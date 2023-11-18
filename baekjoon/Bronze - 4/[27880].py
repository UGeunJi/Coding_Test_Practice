sum = 0

for _ in range(4) :
    a, b = input().split()
    sum += int(b) * [21, 17][a =='Stair']
    
print(sum)
