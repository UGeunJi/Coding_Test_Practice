earn = list(map(int, input().split()))
n = int(input())
s = 0
for i in range(n):
    a, b, c = map(float, input().split())
    if b >= 2.00 and c >=17:
        s += earn[int(a)]
        
print(s)
