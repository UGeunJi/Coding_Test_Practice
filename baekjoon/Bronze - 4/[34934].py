n = int(input())
s, year = 'a', 0
for i in range(n):
    a, b = input().split()
    if int(b) > year:
        s = a
        year = int(b)
        
print(s)
