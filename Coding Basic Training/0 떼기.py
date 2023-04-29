def solution(n_str):
    answer = ''
    idx = 0
    
    for i in range(len(n_str)):
        if n_str[i] != '0':
            idx = i
            break
            
    answer = n_str[i:] 
    
    return answer
