n, m=map(int, input().split())
result = 0
max_result = 0
z = []

for i in range(n):
    z.append(list(map(int, input().strip())))

    one_count = 0
    if z[i][0] == 1:
        one_count += 1

    for j in range(1, m):
        if z[i][j - 1] == 0 and z[i][j] == 1:
            one_count += 1

    if max_result < one_count: 
        max_result = one_count
        result = 1
    elif max_result == one_count:
        result += 1

print(max_result, result)
