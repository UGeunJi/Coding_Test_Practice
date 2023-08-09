a, b = map(int, input().split())

M = (b - a) / 400

print(1 / (1 + 10 ** M))
