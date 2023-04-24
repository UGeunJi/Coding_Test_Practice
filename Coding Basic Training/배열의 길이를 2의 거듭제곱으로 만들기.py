def solution(arr):
    i = 1
    length = len(arr)
    
    if length == 1:
        return arr
    else:
        while True:
            if length < 2 ** i:
                break
            if length == 2 ** i:
                break
            i += 1

        for _ in range(2 ** i - length):
            arr.append(0)
        
    return arr
