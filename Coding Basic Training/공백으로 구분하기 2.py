def solution(my_string):
    answer = my_string.split(' ')
    
    for i in range(len(answer)-1, -1, -1):
        if answer[i] == '':
            answer.remove(answer[i])
            
    return answer
