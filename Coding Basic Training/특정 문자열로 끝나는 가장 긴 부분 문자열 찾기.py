def solution(myString, pat):
    answer = ''
    myString_l = list(myString)
    slice = pat[-1]
    idx = 0
    for i in range(len(myString_l)-1, -1, -1):
        if myString[i] == slice:
            idx = i
            break
        
    answer = myString[:idx + 1]
    
    return answer
