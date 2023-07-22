n = int(input())

for i in range(n):
    num1, num2 = map(int, input().split())
    for j in range(num2):
        print('X' * num1)
    print()
