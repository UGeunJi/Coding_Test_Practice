def solution(arr, query):
    s, e = 0, 0
    
    for i in range(len(query)):
        if i % 2:
            s += query[i]
        else:
            e = s + query[i]
        
    return arr[s:e + 1] if s != e + 1 else [-1]
