def solution(a, b):
    answer = ''
    
    answer += str(a)
    answer += str(b)
    
    num = 2 * a * b
    
    return max(int(answer), num)
