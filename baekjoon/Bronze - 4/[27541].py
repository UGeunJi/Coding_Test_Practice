n = int(input())
s = input()

if s[-1] == 'G':
    print(s[:-1])
else:
    s = list(s)
    s.append('G')
    print(''.join(s))
