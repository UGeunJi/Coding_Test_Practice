def solution(data, ext, val_ext, sort_by):
    answer = []
    if ext == "code":
        pivot = 0
    elif ext == "date":
        pivot = 1
    elif ext == "maximum":
        pivot = 2
    elif ext == "remain":
        pivot = 3
    if sort_by == "code":
        sort_pivot = 0
    elif sort_by == "date":
        sort_pivot = 1
    elif sort_by == "maximum":
        sort_pivot = 2
    elif sort_by == "remain":
        sort_pivot = 3

    for i in range(len(data)):
        if data[i][pivot] < val_ext:
            answer.append(data[i])
            
    answer = sorted(answer, key=lambda x: x[sort_pivot])

    return answer
