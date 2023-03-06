from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    want_list = dict(zip(want, number))
    
    for i in range(len(discount) - sum(number) + 1):
        cnt = dict(Counter(discount[i:i+sum(number)]))
        for j in range(len(want_list)):
            if list(want_list)[j] in cnt:
                if want_list.get(list(want_list)[j]) == cnt.get(list(want_list)[j]):
                    pass
                else:
                    break
            else:
                break
        else:
            answer += 1

    return answer
