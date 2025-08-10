n = int(input())
a_sum = 0
b_sum = 0

for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        a_sum += a + b
    elif a < b:
        b_sum += a + b
    else:
        a_sum += a
        b_sum += b

print(a_sum, b_sum)
