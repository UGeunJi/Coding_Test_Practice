def solution(wallpaper):
    answer = []
    right = bottom = 0
    top = left = 51
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                if top >= i:
                    top = i
                if left >= j:
                    left = j
                if right <= j:
                    right = j + 1
                if bottom <= i:
                    bottom = i + 1
    
    answer.append(top)
    answer.append(left)
    answer.append(bottom)
    answer.append(right)
    
    return answer
