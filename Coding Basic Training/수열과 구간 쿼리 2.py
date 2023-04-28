def solution(arr, queries):
    answer = []
    
    
    for i in range(len(queries)):
        temp = arr[queries[i][0]:queries[i][1] + 1]
        temp_l = []
        
        for j in range(len(temp)):
            if temp[j] > queries[i][2]:
                temp_l.append(temp[j])
                
        if len(temp_l) == 0:
            answer.append(-1)
        else:
            answer.append(min(temp_l))
        
    return answer
