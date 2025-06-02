subjectCode = input()
N = int(input())
result = 0

for _ in range(N):
    availableCode = input()
    if subjectCode[:5] == availableCode[:5]:
        result += 1

print(result)
