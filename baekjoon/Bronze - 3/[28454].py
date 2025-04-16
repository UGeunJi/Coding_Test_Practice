li = list(map(int, input().split('-')))
n = int(input())
num = 0

for _ in range(n):
    a, b, c = map(int, input().split('-'))

    if a < li[0]:
        pass
    elif a == li[0] and b < li[1]:
        pass
    elif a == li[0] and b == li[1] and c < li[2]:
        pass
    else:
        num += 1
        
print(num)
