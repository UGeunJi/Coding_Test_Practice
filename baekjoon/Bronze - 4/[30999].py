a, b = map(int, input().split())
cnt = 0

for i in range(a):
    vote = input()
    if vote.count('O') > (b / 2):
        cnt += 1
    else:
        pass

print(cnt)    
