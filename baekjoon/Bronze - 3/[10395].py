x = list(map(int, input().split()))
y = list(map(int, input().split()))

for i in range(5):
    x[i] += y[i]

print('Y' if x.count(1) == 5 else 'N')
