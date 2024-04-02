li = list(map(int, input().split()))
li.sort()

if li[2] >= li[0] + li[1]:
    print(li[0] + li[1] + (li[0] + li[1] - 1))
else:
    print(li[0] + li[1] + li[2])
