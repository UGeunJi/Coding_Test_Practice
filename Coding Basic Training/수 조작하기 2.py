def solution(numLog):
    answer = ''
    init = numLog[0]
    
    for i in range(1, len(numLog)):
        if numLog[i] - init == -1:
            answer += 's'
            init = numLog[i]
        elif numLog[i] - init == 1:
            answer += 'w'
            init = numLog[i]
        elif numLog[i] - init == -10:
            answer += 'a'
            init = numLog[i]
        elif numLog[i] - init == 10:
            answer += 'd'
            init = numLog[i]
    
    return answer
