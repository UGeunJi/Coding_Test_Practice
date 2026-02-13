n = int(input())
li = []

for i in range(n):
    li.append(int(input()))
    li_2 = sorted(li)

if li[0] == li_2[0]:
    print('ez')
elif li[0] == li_2[-1]:
    print('hard')
else:
    print('?')
