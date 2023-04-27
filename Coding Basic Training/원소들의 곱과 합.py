def solution(num_list):
    answer = 0
    mul = 1
    su = sum(num_list) ** 2
    
    for i in range(len(num_list)):
        mul *= num_list[i]
    
    if mul < su:
        answer = 1
    else:
        answer = 0
    
    return answer
