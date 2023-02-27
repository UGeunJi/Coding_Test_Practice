a = [1, 0, 1]
b = [0, 1, 1]

def f(n):
    l = len(a)
    if n >= l:
        for i in range(l, n + 1):
            a.append(a[i - 1] + a[i - 2])
            b.append(b[i - 1] + b[i - 2])
    print(f'{a[n]} {b[n]}')
    
times = int(input())

for _ in range(times):
    f(int(input()))
