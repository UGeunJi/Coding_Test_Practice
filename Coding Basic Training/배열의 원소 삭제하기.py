def solution(arr, delete_list):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] in delete_list:
            arr.remove(arr[i])
            
    return arr
