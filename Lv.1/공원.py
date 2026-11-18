def solution(mats, park):
    mats.sort(reverse=True)
    rows = len(park)
    cols = len(park[0])

    for size in mats:
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                if all(park[i + y][j : j + size] == ["-1"] * size for y in range(size)):
                    return size
                    
    return -1
