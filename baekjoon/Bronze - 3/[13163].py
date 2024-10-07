n = int(input())

for _ in range(n):
    nn = input().split()
    result = "god"

    for i in range(1, len(nn)):
        result += nn[i]

    print(result)
