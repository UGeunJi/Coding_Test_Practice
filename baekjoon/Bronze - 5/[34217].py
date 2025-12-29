a, b = map(int, input().split())
c, d = map(int, input().split())

if a + c < b + d:
    print("Hanyang Univ.")
elif a + c > b + d:
    print("Yongdap")
else:
    print("Either")
