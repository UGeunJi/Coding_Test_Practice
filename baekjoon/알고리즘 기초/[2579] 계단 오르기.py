n = int(input())
s = [int(input()) for _ in range(n)]
stairs = [0] * n

if len(s) <= 2:
    print(sum(s))

else:
    stairs[0] = s[0]
    stairs[1] = s[0] + s[1]
    
    for i in range(2, n):
        stairs[i] = max(stairs[i - 3] + s[i - 1] + s[i], stairs[i - 2] + s[i])
    
    print(stairs[-1])
