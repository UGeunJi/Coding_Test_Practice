def solution(arr):
    answer = []
    start = -1
    end = -1
    
    for i in range(len(arr)):
        if arr[i] == 2:
            start = i
            break
    
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 2:
            end = i
            break
    
    answer = arr[start:end+1]
    
    if start == -1 or end == -1:
        answer.append(-1)
    
    return answer
