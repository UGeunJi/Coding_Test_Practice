def solution(arr, k):
    answer = []
    base = arr[0]
    answer.append(base)
    
    for i in range(1, len(arr)):
        if arr[i] not in answer:
            answer.append(arr[i])
            base = arr[i]
        if len(answer) == k:
            break
            
    if len(answer) < k:
        for i in range(k - len(answer)):
            answer.append(-1)
            
    return answer
