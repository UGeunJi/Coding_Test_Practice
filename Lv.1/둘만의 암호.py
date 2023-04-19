def solution(s, skip, index):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    
    for i in skip:
        if i in alpha:
            alpha = alpha.replace(i, '')        

    for i in s:
        answer += alpha[(alpha.index(i) + index) % len(alpha)]
    
    return answer
