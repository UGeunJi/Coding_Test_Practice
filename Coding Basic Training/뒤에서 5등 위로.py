def solution(num_list):
    num_list.sort(reverse=True)

    for _ in range(5):
        num_list.pop()

    num_list.reverse()
    
    return num_list
