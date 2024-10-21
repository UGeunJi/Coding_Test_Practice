n = int(input())
s = input()
li = list(reversed(s))

while 1 :
    if li.count('s') == li.count('t'):
        break
    else :
        li.pop(-1)

li.reverse()
print(''.join(li))
