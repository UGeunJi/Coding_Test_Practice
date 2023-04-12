def solution(cards1, cards2, goal):
    answer = ''
    
    for i in range(len(goal)):

        if goal[i] == cards1[0]:
            cards1.pop(0)
            if len(cards1) == 0:
                cards1.append("zero")
        elif goal[i] == cards2[0]:
            cards2.pop(0)
            if len(cards2) == 0:
                cards2.append("zero")
        else:
            answer = "No"
            break

    else:
        answer = "Yes"    

    return answer
