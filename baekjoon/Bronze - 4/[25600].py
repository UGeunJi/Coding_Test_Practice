n = int(input())
score = []

for i in range(n):
    l_init = list(map(int, input().split()))
    if l_init[0] == l_init[1] + l_init[2]:
        score.append((l_init[0] * (l_init[1] + l_init[2])) * 2)
    else:
        score.append(l_init[0] * (l_init[1] + l_init[2]))
        
print(max(score))
