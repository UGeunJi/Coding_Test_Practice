while True:
    i = 1
    sum = 0
    n = int(input())
    if n == 0:
        break
    for _ in range(n):
        sum += i
        i += 1
    print(sum)
    if i == n:
        continue
