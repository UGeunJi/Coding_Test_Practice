from itertools import product

def solution(word):
    dic = []
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat = i):
            dic.append(''.join(list(c)))

    dic.sort()
    return dic.index(word) + 1


#########################################################################################################################################


def solution(word):
    answer = 0
    li  = ['A', 'E', 'I', 'O', 'U','']
    dic = []

    for i in li:
        for j in li:
            for k in li:
                for l in li:
                    for m in li:
                        w = i + j + k + l + m
                        if w not in dic: 
                            dic.append(w)

    dic.sort()
    answer = dic.index(word)

    return answer
