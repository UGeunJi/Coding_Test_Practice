import sys
input = sys.stdin.readline

# 입력
N = int(input())

# 50이 들어가면 +1
res = 0
for i in range(N):
    res += 1
    if str(i).find("50") > -1:
        res += 1
print(res)
