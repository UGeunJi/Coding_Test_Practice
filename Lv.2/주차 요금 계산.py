import math

def solution(fees, records):
    answer = []
    time = []
    num = []
    io = []
    ans = []
    
    for i in range(len(records)):                          # record 시간, 번호, 입차로 나눔
        records[i] = records[i].split()

    for i in range(len(records)):                          # 각 리스트에 저장
        time.append(records[i][0].split(':'))
        num.append(records[i][1])
        io.append(records[i][2])
        
    for i in range(len(time)):                             # 시간 분단위로 바꿔줌
        time[i] = int(time[i][0]) * 60 + int(time[i][1])

    for i in range(len(num)):                              # 누적 주차 시간 계산
        if num[i] == i:                                    # 바꿔준 값이면 그냥 넘김
            continue

        sum = -time[i]                                     # 입차시간
        temp = num[i]                                      # 정렬을 위해 2차원 리스트로 넣어줄 재료
        stack = [0]                                        # 출차 여부를 위한 stack

        for j in range(i + 1, len(num)):                   # 같은 번호 탐색
            if num[i] == num[j] and io[j] == 'IN':         # 입차
                sum -= time[j]
                stack.append(1)
                num[j] = j
            elif num[i] == num[j] and io[j] == 'OUT':      # 출차
                sum += time[j]
                stack.pop()
                num[j] = j

        if len(stack) == 1:                                # 출차하지 않고 하루가 지날 때
            sum += 1439

        if sum <= fees[0]:                                 # 기본 요금
            answer.append([fees[1], temp])
        else:                                              # 기본 요금X
            fee = fees[1] + math.ceil((sum - fees[0]) / fees[2]) * fees[3]
            answer.append([fee, temp])
    
    answer = sorted(answer, key=lambda x:x[1])             # 낮은 번호 순으로 정렬

    for i in range(len(answer)):                           # 정렬 후 요금만
        ans.append(answer[i][0])
    
    return ans
