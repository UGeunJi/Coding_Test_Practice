a, b = map(int, input().split())
n = 1
number = 0

while True:
    number = a * n
    if number >= b:
        print(n)
        break
    else:
        n += 1
