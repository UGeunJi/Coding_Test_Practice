n = int(input())

for i in range(n):
    num = int(input())
    if 17.5 <= num % 25 + 0.5 <= 24.5:
        print('OFFLINE')
    else:
        print('ONLINE')
