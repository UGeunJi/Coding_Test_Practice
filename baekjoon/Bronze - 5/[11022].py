n = int(input())

for i in range(n):
    A, B = map(int, input().split())
    print(f'Case #{i + 1}: {A} + {B} = {A + B}')
