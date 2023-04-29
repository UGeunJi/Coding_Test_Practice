def solution(myString, pat):
    myString = list(myString)
    
    for i in range(len(myString)):
        if myString[i] == 'A':
            myString[i] = 'B'
        else:
            myString[i] = 'A'
    
    myString = ''.join(myString)
    
    if pat in myString:
        return 1
    else:
        return 0
