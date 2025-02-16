n = int(input())
li = [input() for _ in range(n)]

res = sum([int(s[: -1]) ** int(s[-1]) for s in li])

print(res)
