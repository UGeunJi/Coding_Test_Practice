import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
a = max(n - (m * k), 0)
b = n - m * (k - 1) - 1

print(a, b)
