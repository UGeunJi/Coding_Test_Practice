n = int(input())
li = []

for i in range(n):
    li.append(input())
    
if li.index('yonsei') < li.index('korea'):
    print('Yonsei Won!')
else:
    print('Yonsei Lost...')
