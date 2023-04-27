def solution(l, r):
    answer = []
    
    for i in range(l, r + 1):
        if i % 5 == 0:
            if '1' not in str(i) and '2' not in str(i) and '3' not in str(i) and '4' not in str(i) and '6' not in str(i) and '7' not in str(i) and '8' not in str(i) and '9' not in str(i):
                answer.append(i)
    
    if len(answer) == 0:
        answer.append(-1)
        
    return answer
