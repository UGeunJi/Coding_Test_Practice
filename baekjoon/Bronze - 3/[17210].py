n = int(input())
a = int(input())
if n <= 5:
    for i in range(n - 1):
        a = int(not a)
        print(a)
else:
    print("Love is open door")
