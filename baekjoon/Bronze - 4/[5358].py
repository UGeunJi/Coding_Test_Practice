while True:
    try:      
        answer = ''
        s = input()
        
        for j in s:
            if j == 'i':
                j = 'e'
            elif j == 'e':
                j = 'i'
            elif j == 'I':
                j = 'E'
            elif j == 'E':
                j = 'I'
            
            answer += j

        print(answer)

    except EOFError:
        break    
