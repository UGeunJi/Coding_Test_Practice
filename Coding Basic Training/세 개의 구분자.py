def solution(myStr):
    l = list(myStr)
    
    for i in range(len(l)):
        if l[i] == 'a':
            l[i] = ' '
        elif l[i] == 'b':
            l[i] = ' '
        elif l[i] == 'c':
            l[i] = ' '
            
    s = ''.join(l)
    answer = s.split(' ')
    
    for i in range(len(answer)-1, -1, -1):
        if answer[i] == '':
            answer.remove(answer[i])
    
    if len(answer) == 0:
        answer.append('EMPTY')

    return answer
