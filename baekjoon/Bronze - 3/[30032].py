N, D = map(int, input().split())

for i in range(0, N) : 
    str = input()
    result = ''
    
    for j in range (0, N) : 
        
        if D == 1 : 
            if str[j] == 'd' : 
                result += 'q'
            elif str[j] == 'b' : 
                result += 'p'
            elif str[j] == 'q' : 
                result += 'd'
            elif str[j] == 'p' : 
                result += 'b'
        
        elif D == 2 : 
            if str[j] == 'd' : 
                result += 'b'
            elif str[j] == 'b' : 
                result += 'd'
            elif str[j] == 'q' : 
                result += 'p'
            elif str[j] == 'p' : 
                result += 'q'

    print(result)
