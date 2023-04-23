def solution(arr, k):
    answer = []
    if k % 2 == 0:
        for i in range(len(arr)):
            arr[i] += k
    else:
        for i in range(len(arr)):
            arr[i] *= k
            
    return arr
