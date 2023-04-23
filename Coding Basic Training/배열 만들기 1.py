def solution(n, k):
    answer = []
    i = 1
    
    while True:
        num = k * i
        if num > n:
            break
            
        answer.append(num)
        i += 1
        
    return answer
