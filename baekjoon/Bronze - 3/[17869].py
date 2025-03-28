cnt = 0
n = int(input())

while n != 1:
    n = n + 1 if n % 2 == 1 else n //2
    cnt += 1

print(cnt)
