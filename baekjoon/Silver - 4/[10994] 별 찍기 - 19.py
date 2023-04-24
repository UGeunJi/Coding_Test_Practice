n = int(input())
stars = [[' ' for _ in range(4 * n - 3)] for _ in range(4 * n - 3)]  # 뼈대 구성

def answer(n, x, y):
    if n == 1:
        stars[y][x] = '*'
        return

    l = 4 * n - 3

    for i in range(l):
        stars[y][x + i] = '*'             # 위
        stars[y + i][x] = '*'             # 왼쪽
        stars[y + l - 1][x + i] = '*'     # 아래
        stars[y + i][x + l - 1] = '*'     # 오른쪽
    
    answer(n - 1, x + 2, y + 2)           # n이 작아지면서 필요한 부분의 공백에 * 추가

answer(n, 0, 0)

for s in stars:
    print(''.join(s))
