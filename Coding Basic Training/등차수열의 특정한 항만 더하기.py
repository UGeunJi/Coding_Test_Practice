def solution(a, d, included):
    answer = 0
    pivot = a
    
    for i in range(len(included)):
        if included[i] == True:
            answer += pivot
        
        pivot += d
    
    return answer
