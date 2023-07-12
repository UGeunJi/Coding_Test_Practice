a, b = map(int, input().split())
l_init = list(map(int, input().split()))
l_min = []

for i in range(len(l_init) - 1):
    l_min.append(l_init[i] + l_init[i + 1])

answer = min(l_min) * b
print(answer)
