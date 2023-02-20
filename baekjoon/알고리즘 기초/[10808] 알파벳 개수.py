s = input()

answer = [0] * 26

for i in s:
    answer[ord(i) - 97] += 1

print(*answer)
