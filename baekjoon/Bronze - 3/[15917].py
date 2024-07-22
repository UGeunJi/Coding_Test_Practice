import sys
n = int(sys.stdin.readline())

a = [2 ** num for num in range(32)]

for i in range(n):
    s = int(sys.stdin.readline())
    if s in a:
        print(1)
    else:
        print(0)
