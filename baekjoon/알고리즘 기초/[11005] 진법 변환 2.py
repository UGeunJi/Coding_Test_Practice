num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
n, b = map(int, input().split())

answer = ''
while n:
    rest = n % b
    n //= b
    answer += num[rest]

print(answer[::-1])
