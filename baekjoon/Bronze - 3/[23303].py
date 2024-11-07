s = input()
a = 0
for i in range(len(s) - 1):
    if s[i : i + 2] == 'D2' or s[i : i + 2] == 'd2':
        a = 1
        break
    else:
        a = 0

if a == 1:
    print('D2')
else:
    print('unrated')
