l, d = int(input()), int(input())
x = int(input())

for i in range(l, d + 1):
    if sum(map(int, list(str(i)))) == x:
        print(i)
        break
        
for i in range(d, l - 1, -1):
    if sum(map(int, list(str(i)))) == x:
        print(i)
        break
