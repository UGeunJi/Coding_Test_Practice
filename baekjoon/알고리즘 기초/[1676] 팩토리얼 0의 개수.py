import math

f = math.factorial(int(input()))
f = list(str(f)[::-1])

answer = 0

for i in range(len(f)):
    if f[i] != '0':
        break
    elif f[i] == '0':
        answer += 1

print(answer)
