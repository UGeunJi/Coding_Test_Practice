def snail(n):
    arr = [[0 for j in range(n)] for i in range(n)]
    row = 0
    col = -1
    cnt = 1
    trans = 1
    
    while n > 0:
        for i in range(n):
            col += trans
            arr[row][col] = cnt
            cnt += 1
        n -= 1
        
        for j in range(n):
            row += trans
            arr[row][col] = cnt
            cnt += 1
        trans *= -1
        
    return arr

def solution(n):
    arr = snail(n)
    return arr
