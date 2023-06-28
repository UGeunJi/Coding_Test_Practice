num = int(input())

print("Gnomes:")

for i in range(num):
    a, b, c = map(int, input().split())
    l = []
    l.append(a)
    l.append(b)
    l.append(c)
    
    if sorted(l, reverse=True) == l or sorted(l, reverse=False) == l:
        print("Ordered")
    else:
        print("Unordered")
