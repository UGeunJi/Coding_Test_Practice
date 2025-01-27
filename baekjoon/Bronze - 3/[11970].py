import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

if c >= b or d <= a:
    print(b - a + d - c)
else:
    print( max(b, d) - min(a, c))
