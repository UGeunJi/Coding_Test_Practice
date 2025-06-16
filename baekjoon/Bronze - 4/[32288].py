n = int(input())
s = input()
blink = ''
for i in s:
    if i == 'I':
        blink += 'i'
    else:
        blink += 'L'

print(blink)
