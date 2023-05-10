def solution(park, routes):
    log = []
    temp = []

    for i in range(len(park)):               # park 이중리스트화
        park[i] = list(park[i])

    for i in range(len(routes)):             # routes 방향과 수 구분
        routes[i] = routes[i].split()
        routes[i][1] = int(routes[i][1])

    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':            # 시작점 지정
                log = [i, j]

    for a in range(len(routes)):
        if routes[a][0] == 'N':                                         # N일 때
            if log[0] - routes[a][1] < 0:                               # 네모를 벗어날 때
                continue
            else:                                                       # 네모를 벗어나지 않을 때
                for k in range(1, routes[a][1] + 1):                    # X 찾기 위한 for문
                    if park[log[0] - k][log[1]] == 'X':                 # X면
                        temp = [log[0], log[1]]
                        break                                           # 넘어가라
                    else:                                               # X가 아니면
                        temp = [log[0] - routes[a][1], log[1]]          # temp update

                log = temp

        elif routes[a][0] == 'S':                                       # S 일 때
            if log[0] + routes[a][1] >=  len(park):       
                continue
            else:                                    
                for k in range(1, routes[a][1] + 1):    
                    if park[log[0] + k][log[1]] == 'X':       
                        temp = [log[0], log[1]]
                        break
                    else:
                        temp = [log[0] + routes[a][1], log[1]]

                log = temp

        elif routes[a][0] == 'W':                                      # W 일 때
            if log[1] - routes[a][1] < 0:       
                continue
            else:                                    
                for k in range(1, routes[a][1] + 1):    
                    if park[log[0]][log[1] - k] == 'X':       
                        temp = [log[0], log[1]]
                        break
                    else:
                        temp = [log[0], log[1] - routes[a][1]]

                log = temp

        elif routes[a][0] == 'E':                                     # E 일 때
            if log[1] + routes[a][1] >= len(park[0]):       
                continue
            else:                                    
                for k in range(1, routes[a][1] + 1):    
                    if park[log[0]][log[1] + k] == 'X':       
                        temp = [log[0], log[1]]
                        break
                    else:
                        temp = [log[0], log[1] + routes[a][1]]

                log = temp

    return log
