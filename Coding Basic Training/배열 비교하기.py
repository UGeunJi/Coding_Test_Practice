def solution(arr1, arr2):
    answer = 0
    
    if len(arr1) != len(arr2):
        if len(arr1) > len(arr2):
            answer = 1
        else:
            answer = -1
    else:
        if sum(arr1) > sum(arr2):
            answer = 1
        elif sum(arr1) == sum(arr2):
            answer = 0
        else:
            answer = -1
            
    return answer
