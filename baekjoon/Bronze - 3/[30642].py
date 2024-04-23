n = int(input())
a = input()
k = int(input())

if a == "annyong":
    if k % 2 == 1:
        print(k)
    else:
        print(k + 1 if k + 1 <= n else k - 1)
elif a == "induck":
    if k % 2 == 0:
        print(k)
    else:
        print(k + 1 if k + 1 <= n else k - 1)
