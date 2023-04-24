def solution(picture, k):
    answer = []
    
    for i in range(len(picture)):
        temp = ''
        for j in range(len(picture[i])):
            temp += picture[i][j] * k
        
        for _ in range(k):
            answer.append(temp)

    return answer
