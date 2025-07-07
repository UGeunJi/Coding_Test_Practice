n, m = map(int, input().split())
board = [[0] * m for _ in range(n)]
for i in range(n) :
    line = input()
    for j in range(m) :
        board[i][j] = ['W', 'B'][line[j] == 'W']

input()
cnt = 0

for i in range(n) :
    line = input()
    for j in range(m) :
        if line[j] != board[i][j] : cnt += 1

print(cnt)
