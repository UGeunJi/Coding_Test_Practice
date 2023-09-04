n = int(input())
level = list(map(int, input().split()))

for i in range(len(level)):
    if level[i] == 300:
        level[i] = 1
    elif 275 <= level[i] < 300:
        level[i] = 2
    elif 250 <= level[i] < 275:
        level[i] = 3
    elif level[i] < 250:
        level[i] = 4
        
print(*level)
