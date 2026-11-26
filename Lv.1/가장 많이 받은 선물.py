def solution(friends, gifts):
    answer = 0
    container = []
    score = []

    for i in range(len(friends)):
        container.append([0, 0])
        score.append(0)

    for i in range(len(gifts)):
        gifts[i] = gifts[i].split()

    for j in range(len(gifts)):
        container[friends.index(gifts[j][0])][0] += 1
        container[friends.index(gifts[j][1])][1] += 1
    for q in range(len(container)):
        container[q] = container[q][0] - container[q][1]

    for x in range(len(friends)):
        for y in range(x + 1, len(friends)):
            temp1, temp2 = 0, 0
            for z in range(len(gifts)):
                if gifts[z][0] == friends[x] and gifts[z][1] == friends[y]:
                    temp1 += 1
                elif gifts[z][0] == friends[y] and gifts[z][1] == friends[x]:
                    temp2 += 1

            if temp1 > temp2:
                score[x] += 1
            elif temp1 < temp2:
                score[y] += 1
            elif temp1 == temp2:
                if container[x] > container[y]:
                    score[x] += 1
                elif container[x] < container[y]:
                    score[y] += 1

    answer = max(score)
                
    return answer
