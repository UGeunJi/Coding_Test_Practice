def solution(str_list):
    answer = []
    str_list = ''.join(str_list)
    
    for i in range(len(str_list)):
        if str_list[i] == 'l':
            answer = str_list[:i]
            break
        elif str_list[i] == 'r':
            answer = str_list[i + 1:]
            break
    
    if len(answer) == 0:
        return []
    else:
        return list(answer)
