n1 = int(input())

for j in range(n1):
    n2 = int(input())
    
    for i in range(n2):
        a, b = map(int, input().split())

        l = []
        l.append(a + b), l.append(a * b)
    
        print(*l)
