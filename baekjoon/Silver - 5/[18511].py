from itertools import product

n, k_num = map(int, input().split())
len_max = len(str(n))
k = list(input().split())

while True:
    tmp = list(product(k, repeat = len_max)) #repeat를 통해 몇 개를 뽑을지 결정
    result = []

    for i in tmp:
        if int("".join(i)) <= n:
            result.append(int("".join(i)))
    
    if len(result) >= 1:
        print(max(result))
        break
    
    else:
        len_max -= 1
