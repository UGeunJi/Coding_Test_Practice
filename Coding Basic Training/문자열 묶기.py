def solution(strArr):
    answer = 0
    arr = []
    
    strArr.sort(key = lambda x:len(x))
    
    for i in range(1, len(strArr[-1]) + 1):
        cnt = 0
        for j in range(len(strArr)):
            if len(strArr[j]) == i:
                cnt += 1
            
        arr.append(cnt)
    
    answer = max(arr)
    
    return answer
