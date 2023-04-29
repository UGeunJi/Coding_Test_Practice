def solution(n):
    answer = []
    
    for i in range(n):
        arr = []
        for j in range(n):
            if i == j:
                arr.append(1)
            else:
                arr.append(0)

        answer.append(arr)
    
    return answer
