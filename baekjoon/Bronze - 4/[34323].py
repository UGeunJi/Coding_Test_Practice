n, m, s = map(int, input().split())

print(min(s * (m + 1) * (100 - n) // 100, s * m))
