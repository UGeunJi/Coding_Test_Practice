def solution(n):
    answer = 0
    i = 1
    j = 2
    
    if n % 2 == 1:
        while True:
            answer += i
            if i == n:
                break
            i += 2
            
    else:
        while True:
            answer += j ** 2
            if j == n:
                break
            j += 2
            
    return answer
