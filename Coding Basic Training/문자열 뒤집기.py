def solution(my_string, s, e):
    answer = ''
    
    start = my_string[:s]
    middle = my_string[s : e + 1][::-1]
    end = my_string[e+1:]
    
    answer = start + middle + end
    
    return answer
