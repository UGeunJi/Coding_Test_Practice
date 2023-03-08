def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        lower = i + 1
        for j in range(i+1, len(prices)):
            lower += 1
            if prices[i] > prices[j]:
                break

        answer.append(lower - (i + 1))

    return answer
