def solution(rank, attendance):
    answer = 0
    arr = []
    
    for _ in range(len(rank)):
        r = min(rank)
        if attendance[rank.index(r)] == True:
            arr.append(rank.index(r))
            rank[rank.index(r)] = 101
        else:
            rank[rank.index(r)] = 101
        
        if len(arr) == 3:
            break
            
    answer = 10000 * arr[0] + 100 * arr[1] + arr[2]
    
    return answer
