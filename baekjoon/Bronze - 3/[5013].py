cnt = 0

for _ in range(int(input())) :
    s = input()
    win = True
    for i in range(1, len(s)) :
        if s[i - 1] == "C" and s[i] == "D" : win = False
    if win : cnt += 1

print(cnt)
