n = int(input())

for i in range(n):
    temp = []
    num = bin(int(input()))[2:]
    num_l = list(num)[::-1]
    
    for j in range(len(num_l)):
        if num_l[j] == '1':
            temp.append(j)
    
    print(*temp)
