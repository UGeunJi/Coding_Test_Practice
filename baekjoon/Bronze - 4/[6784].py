n = int(input()) * 2
a, b = [], []

for i in range(n):
    if i < n // 2:
        a.append(input())
    else:
        b.append(input())

score = 0

for j in range(len(a)):
    if a[j] == b[j]:
        score += 1
        
print(score)
