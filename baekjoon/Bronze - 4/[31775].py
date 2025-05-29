gp = [input() for _ in range(3)]
l = k = p = False

for i in gp:
    if i[0] == "l":
        l = True
    elif i[0] == "k":
        k = True
    elif i[0] == "p":
        p = True

if l == k == p == True:
    print("GLOBAL")
else:
    print("PONIX")
