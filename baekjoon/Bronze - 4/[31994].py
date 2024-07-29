a, b = [], []
for i in range(7):
    l, n = map(str, input().split())
    a.append(l)
    b.append(int(n))

m_num = b.index(max(b))
print(a[m_num])
