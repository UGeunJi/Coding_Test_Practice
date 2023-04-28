def solution(x1, x2, x3, x4):
    answer = True
    
    if x1 == True or x2 == True:
        X1 = True
    else:
        X1 = False
    
    if x3 == True or x4 == True:
        X2 = True
    else:
        X2 = False
    
    if X1 == False or X2 == False:
        answer = False
    
    return answer
