def solution(my_string, overwrite_string, s):
    answer = ''
    
    s_start = my_string[:s]
    s_end = my_string[s + len(overwrite_string) :]
    
    answer = s_start + overwrite_string + s_end
    
    return answer
