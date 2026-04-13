from collections import Counter

a, b, c = map(int, input().split())
li = []

for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            li.append(i + j + k)

counter = Counter(li)
mode = counter.most_common(1)

print(mode[0][0])
