def solution(myString):
    myString = myString.split('x')
    myString.sort()
    
    for i in range(len(myString)-1, -1, -1):
        if myString[i] == '':
            myString.remove(myString[i])
    
    return myString
