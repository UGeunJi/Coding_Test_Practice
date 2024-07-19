n = int(input())

seat = []
for a in range(10):
    seat.append([])
    for b in range(20):
        seat[a].append('.')
    
for i in range(n):
    s = input()
    r = ord(s[0])
    c = int(s[1:])
    seat[r - 65][c - 1] = 'o'

for i in range(10):
    for j in range(20):
        print(seat[i][j], end='')
    print()
