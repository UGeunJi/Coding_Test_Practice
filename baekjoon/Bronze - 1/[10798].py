dir = []
anchor = 0
for i in range(5):
    dir.append(list(input()))
    if len(dir[i]) > anchor:
        anchor = len(dir[i])

for j in range(5):
    for k in range(anchor):
        tmp = anchor - len(dir[j])
        for l in range(tmp):
            dir[j].append('$')

answer = ''
for x in range(anchor):
    for y in range(5):
        if dir[y][x] == '$':
            pass
        else:
            answer += dir[y][x]

print(answer)
