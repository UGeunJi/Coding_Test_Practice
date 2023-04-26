def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif len(stk) != 0 and stk[-1] == arr[i]:
            stk.pop()
            i += 1
        elif len(stk) != 0 and stk[-1] != arr[i]:
            stk.append(arr[i])
            i += 1
    
    if len(stk) == 0:
        return [-1]
    else:
        return stk
