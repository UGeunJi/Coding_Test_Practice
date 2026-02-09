n = int(input())
l_temp = []

for i in range(n):
    l_temp = list(map(int, input().split()))
    for j in range(len(l_temp) - 2):
        if l_temp[j + 1] * 2 <= l_temp[j + 2]:
            if j == len(l_temp) - 3:
                print('Denominations:', *l_temp[1:])
                print('Good coin denominations!')
        else:
            print('Denominations:', *l_temp[1:])
            print('Bad coin denominations!')
            break
    if i != n - 1:
        print()
