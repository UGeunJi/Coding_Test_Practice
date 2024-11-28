import sys
input = sys.stdin.readline

s = int(input().rstrip())
c = input().count('e')

print(['2', 'e', 'yee'][(c > s - c) + ((s - c) == c) * 2])
