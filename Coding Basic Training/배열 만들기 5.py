def solution(intStrs, k, s, l):
    answer = []
    
    for i in range(len(intStrs)):
        if int(intStrs[i][s : s + l]) > k:
            answer.append(int(intStrs[i][s : s + l]))
            
    return answer
