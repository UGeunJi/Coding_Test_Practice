n = int(input())

for _ in range(n):
    A, B = map(int, input().split())
    d = B - A
    cnt = 0  
    m = 1
    mm = 0 
    
    while mm < d :
        cnt += 1
        mm += m 
        if cnt % 2 == 0 :   
            m += 1  
            
    print(cnt)
