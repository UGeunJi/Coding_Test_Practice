import sys

n = int(input().rstrip())

for _ in range(n):
    temp1 = input().rstrip()
    temp2 = temp1[-2:]
    
    if (int(temp1) + 1) % int(temp2) == 0:
        print('Good')
    else:
        print('Bye')
