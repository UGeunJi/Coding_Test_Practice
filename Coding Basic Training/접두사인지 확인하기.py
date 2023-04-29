def solution(my_string, is_prefix):
    answer = []
    my_string = list(my_string)
    temp = ''
    
    for i in range(len(my_string)):
        temp += my_string[i]
        answer.append(temp)
    
    if is_prefix in answer:
        return 1
    else:
        return 0
