def solution(arr, intervals):
    answer = []
    
    for i in range(len(intervals)):
        for j in range(intervals[i][0], intervals[i][1] + 1):
            answer.append(arr[j])
            
    return answer
