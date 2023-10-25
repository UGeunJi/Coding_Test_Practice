a, b, c = map(int, input().split())

res = max([a, b, c]) * 3 - sum([a, b, c])
print(res)
