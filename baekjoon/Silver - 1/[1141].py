import sys

n = int(sys.stdin.readline())
words = [(input()) for _ in range(n)]

words.sort(key=len)

cnt = 0

for i in range(n):
    for j in range(i + 1, n):
        if words[i] == words[j][0:len(words[i])]:
            break
    else:
        cnt += 1

print(cnt)
