a, b = map(int, input().split())
n = int(input())

arr = list(map(int, input().split()))
arr.reverse()

sum = 0
for i in range(n):
    sum += arr[i] * (a ** i)

answer = []

while sum // b:
    answer.append(sum % b)
    sum //= b

answer.append(sum)

print(' '.join(map(str, reversed(answer))))
