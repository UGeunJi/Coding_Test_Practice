x, y, z = map(int, input().split())
u, v, w = map(int, input().split())

print((x * u // 100) + (y * v // 50) + (z * w // 20))
