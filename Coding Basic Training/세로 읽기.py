def solution(my_string, m, c):
    answer = ''

    while c <= len(my_string):
        answer += my_string[c - 1]
        c += m
        
    return answer
