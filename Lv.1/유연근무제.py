def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        tmp = 0
        if (schedules[i] + 10) % 100 >= 60:
            schedules[i] += 50
        else:
            schedules[i] += 10
        
        for j in range(7):
            if startday == 1:
                pass_index1, pass_index2 = 5, 6
            elif startday == 2:
                pass_index1, pass_index2 = 4, 5
            elif startday == 3:
                pass_index1, pass_index2 = 3, 4
            elif startday == 4:
                pass_index1, pass_index2 = 2, 3
            elif startday == 5:
                pass_index1, pass_index2 = 1, 2
            elif startday == 6:
                pass_index1, pass_index2 = 0, 1
            elif startday == 7:
                pass_index1, pass_index2 = 6, 0   

            if j == pass_index1 or j == pass_index2:
                continue
            elif timelogs[i][j] <= schedules[i]:
                tmp += 1
            elif timelogs[i][j] > schedules[i]:
                break
            
            if tmp == 5:
                answer += 1

    return answer
