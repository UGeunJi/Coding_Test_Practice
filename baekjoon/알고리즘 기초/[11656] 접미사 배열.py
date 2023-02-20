s = input()[::-1]

answer = []
subfix = ''

for i in s:
    subfix += i
    answer.append(subfix[::-1])

answer.sort()

print(*answer, sep='\n')
