def solution(signals):
    answer = 0
    pattern = []

    for i in range(len(signals)):
        tmp = []
        for j in range(3):
            if j == 0:
                for k in range(signals[i][j]):
                    tmp.append("green")
            elif j == 1:
                for k in range(signals[i][j]):
                    tmp.append("yellow")
            elif j == 2:
                for k in range(signals[i][j]):
                    tmp.append("red")
        pattern.append(tmp)

    pivot = 0
    sec = 1
    while True:
        for x in range(len(pattern)):
            am = x
            if pattern[x][0] != "yellow":
                break
        
        if am == len(pattern) - 1 and pattern[x][0] == "yellow":
            pivot = 1
        else:
            pivot = 0

        if pivot == 1:
            answer = sec
            break
        else:
            sec += 1
                
        for y in range(len(pattern)):
            pattern[y].append(pattern[y][0])
            pattern[y].pop(0)
            
        if sec >= 10000000:
            return -1
            break

    return answer
