n = int(input())
li = list(map(int, input().split()))

print(li[0] + (n * (li[1] - li[0])))
