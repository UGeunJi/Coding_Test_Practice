def solution(my_string):
    string = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    answer = [0] * 52
    
    for i in my_string:
        answer[string.index(i)] += 1
    
    return answer
