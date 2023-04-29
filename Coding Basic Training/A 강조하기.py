def solution(myString):
    answer = ''
    
    myString = myString.lower()
    myString = list(myString)
    
    for i in range(len(myString)):
        if myString[i] == 'a':
            myString[i] = myString[i].upper()
        
    answer = ''.join(myString)
    
    return answer
