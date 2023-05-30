l = list(map(int, input().split()))

if l[1] < l[2]:
    print("Bus")
elif l[1] > l[2]:
    print("Subway")
else:
    print("Anything")
