def solution(a, b):
    answer1 = ''
    answer2 = ''
    
    answer1 += str(a)
    answer1 += str(b)
    
    answer2 += str(b)
    answer2 += str(a)
    
    answer = max(int(answer1), int(answer2))
    
    return answer
