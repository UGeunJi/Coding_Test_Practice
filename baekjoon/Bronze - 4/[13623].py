l = list(map(int, input().split()))
 
if l[0] == l[1] and l[0] == l[-1]:
    print("*")
elif l[0] != l[1] and l[0] != l[-1] and l[1] == l[-1]:
    print("A")
elif l[1] != l[0] and l[1] != l[-1] and l[0] == l[-1]:
    print("B")
else:
    print("C")
