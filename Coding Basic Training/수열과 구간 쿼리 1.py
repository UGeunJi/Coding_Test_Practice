def solution(arr, queries):
    for i in range(len(queries)):
        for j in range(queries[i][0], queries[i][1] + 1):
            arr[j] += 1
            
    return arr
