def solution(n, m, section):
    answer = 0
    temp = section[0] - 1
    for i in range(0, len(section)):
        if section[i] > temp:
            answer += 1
            temp = section[i] + m - 1
            
    return answer
