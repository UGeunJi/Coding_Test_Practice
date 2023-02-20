import sys

n = int(sys.stdin.readline())
negbin = ''

if not n:
    sys.stdout.write('0')
    exit()

while n:
    rest = abs(n % -2)
    if n % -2:
        n = n // -2 + 1
    else:
        n = n // -2
    negbin += str(rest)

print(negbin[::-1])
