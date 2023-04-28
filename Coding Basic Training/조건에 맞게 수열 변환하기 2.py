import copy

def solution(arr):
    answer = 0
    temp = []
    
    while True:
        if temp == arr:
            break
            
        temp = copy.deepcopy(arr)
        
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] /= 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1
                
        answer += 1
    
    return answer - 1
