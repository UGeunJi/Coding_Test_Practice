def solution(keymap, targets):
    answer = []
    
    for i in range(len(keymap)):
        keymap[i] = list(keymap[i])
    
    for i in range(len(targets)):
        sum = 0
        for j in targets[i]:
            temp = 102
            for k in range(len(keymap)):
                for l in keymap[k]:
                    if j == l and temp > keymap[k].index(l) + 1:
                        temp = keymap[k].index(l) + 1
                        break
                    
            if temp == 102:
                sum = -1
                break
            else:
                sum += temp
            
        answer.append(sum)
        
    return answer
