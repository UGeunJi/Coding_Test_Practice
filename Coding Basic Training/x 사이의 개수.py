def solution(myString):
    answer = []
    myString = myString.split('x')
    
    for i in range(len(myString)):
        answer.append(len(myString[i]))
        
    return answer
