N = int(input())
Bus = []
result1 = result2 = 0

for _ in range(N):
    D, C = input().split()
    Bus.append([D, int(C)])
    if D == "jinju":
        result1 = int(C)

for i in Bus:
    if i[1] > result1:
        result2 += 1

print(result1)
print(result2)
