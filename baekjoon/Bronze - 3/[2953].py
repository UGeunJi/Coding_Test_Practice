total = []
for _ in range(5):
    score = list(map(int, input().split()))
    total.append(sum(score))
print(total.index(max(total)) + 1, max(total)
