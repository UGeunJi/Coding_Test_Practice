def solution(a, b, c, d):
    answer = 0
    p = 0
    q = 0
    r = 0
    
    arr = [a, b, c, d]
    arr_s = set(arr)
    arr_l = list(arr_s)
    
    if len(arr_s) == 1:        # 1번 case
        answer = 1111 * a
        
    elif len(arr_s) == 4:      # 5번 case
        answer = min(arr_l)
        
    elif len(arr_s) == 3:      # 4번 case
        for i in arr_s:
            if arr.count(i) == 2:
                p = i
                break
                
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == p:
                arr.remove(arr[i])
            elif arr[i] != p and q == 0:
                q = arr[i]
                arr.remove(q)
            elif arr[i] != p and r == 0:
                r = arr[i]
                arr.remove(r)
                
        answer = q * r
        
    elif len(arr_s) == 2:       # 3번 case
        if arr.count(arr[0]) == 2:
            p = arr[0]
            for i in arr:
                if i != p:
                    q = i
                else:
                    continue
                    
            answer = (p + q) * abs(p - q)
            
        else:                   # 2번 case
            for i in arr_s:
                if arr.count(i) == 3:
                    p = i
                else:
                    q = i
            
            answer = (10 * p + q) ** 2
                
    return answer
