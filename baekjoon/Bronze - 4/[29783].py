num = int(input())

for i in range(num):
    n = int(input())
    temp = 'Round 1'
    
    if n <= 25:
        temp = 'World Finals'
    elif n <= 1000:
        temp = 'Round 3'
    elif n <= 4500:
        temp = 'Round 2'
        
    print(f'Case #{i + 1}: {temp}')
