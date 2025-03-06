n = int(input())
w = input()
h, i, a, r, c = 0, 0, 0, 0, 0

for i in w:
    if i == 'H':
        h += 1
    elif i == 'I':
        i += 1
    elif i == 'A':
        a += 1
    elif i == 'R':
        r += 1
    elif i == 'C':
        c += 1

print(min(h, i, a, r, c))
