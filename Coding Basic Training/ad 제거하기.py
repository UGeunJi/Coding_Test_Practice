def solution(strArr):
    for i in range(len(strArr)-1, -1, -1):
        if 'ad' in strArr[i]:
            strArr.remove(strArr[i])
            
    return strArr
