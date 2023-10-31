a, b, c = map(int, input().split())

x = 229 * 324 * a * 2
y = 297 * 420 * b * 2
z = 210 * 297 * c

print('{:.6f}'.format((x + y + z) * 0.000001))
