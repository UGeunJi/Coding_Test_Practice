d = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
b = 0

for j in range(len(a)):
    for i in d:
        if a[j] in i:
            b += d.index(i) + 3

print(b)
