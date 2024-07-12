n, m = map(int, input().split())
answer = 'Accepted'

for _ in range(n):
    a, b = map(int, input().split())
    if a == b:
        pass
    else:
        answer = 'Wrong Answer'

if answer == 'Accepted':        
    for _ in range(m):
        c, d = map(int, input().split())
        if c == d:
            pass
        else:
            answer = 'Why Wrong!!!'
        
print(answer)        
