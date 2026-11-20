def solution(n, w, num):
    answer = 0
    number = []
    container = []
    for z in range(n):
        number.append(z + 1)
    for i in range(n // w + 1):
        if i == n // w:
            tmp = number[i * w:]
            if i % 2 == 1:
                tmp = sorted(tmp, reverse=True)
                for i in range(w - len(tmp)):
                    tmp.insert(0, 0)
            else:
                for i in range(w - len(tmp)):
                    tmp.append(0)
            container.append(tmp)
        elif i % 2 == 0:
            tmp = number[i * w:(i + 1) * w]
            container.append(tmp)
        else:
            tmp = number[i * w:(i + 1) * w]
            container.append(sorted(tmp, reverse=True))
    
    anchor = 100000
    for j in range(len(container)):
        if num in container[j]:
            anchor = container[j].index(num)
            print(anchor)
        if anchor != 100000 and container[j][anchor] != 0:
            answer += 1
            
    return answer
