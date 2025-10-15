import sys

n = int(sys.stdin.readline().rstrip())

def SumOfDigits(n):
    sum = 0

    while n > 0:
        sum += (n % 10)
        n //= 10
    
    return sum

sum = SumOfDigits(n)

if n % sum != 0:
    while True:
        n += 1
        sum = SumOfDigits(n)

        if n % sum == 0:
            break

print(n)
