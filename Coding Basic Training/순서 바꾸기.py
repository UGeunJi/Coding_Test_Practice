def solution(num_list, n):
    answer = []
    
    prefix = num_list[n:]
    suffix = num_list[:n]
    
    answer = prefix + suffix
    
    return answer
