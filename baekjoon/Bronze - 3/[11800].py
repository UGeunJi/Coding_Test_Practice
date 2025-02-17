T = int(input())
L = []
K = []
P = ''

for i in range (T):
    a, b = map(int, input().split())
    K.append(a)
    K.append(b)
    K.sort(reverse = True)

    if a == b:
        if a == 1:
            L.append("Habb Yakk")
        elif a == 2:
            L.append("Dobara")
        elif a == 3:
            L.append("Dousa")
        elif a == 4:
            L.append("Dorgy")
        elif a == 5:
            L.append("Dabash")
        elif a == 6:
            L.append("Dosh")
    elif (a == 5 and b == 6) or (a == 6 and b == 5):
        L.append("Sheesh Beesh")
    else:
        for j in K:
            if j == 6:
                P += "Sheesh"
            elif j == 5:
                P += "Bang"
            elif j == 4:
                P += "Ghar"
            elif j == 3:
                P += "Seh"
            elif j == 2:
                P += "Doh"
            elif j == 1:
                P += "Yakk"
            P += " "
        L.append(P)

    K = []
    P = ''
    
for u in range (T):
    print("Case %d: %s" %(u + 1, L[u]))
