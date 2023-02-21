n = int(input())

if n == 1:
    print('')

temp = n

arr = []
i = 1

while i != temp:
    i += 1

    if n % i == 0:
        while n % i == 0:
            print(i)
            n /= i
