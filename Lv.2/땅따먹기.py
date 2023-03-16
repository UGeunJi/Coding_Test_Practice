def solution(land):
    answer = 0

    N = len(land) # N은 행의 개수

    for i in range(0, N-1):
        land[i + 1][0] += max(land[i][1], land[i][2], land[i][3])
        # i + 1번째 행에 0번째 열에는 i번째 행에 1, 2, 3 열 중 최대값을 더해준다. 이런식으로 계속 더해나가면
        # N - 1번째에 열들을 각 선택지에서 가질 수 있는 최대값이 된다.
        land[i + 1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i + 1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i + 1][3] += max(land[i][0], land[i][1], land[i][2])

    answer = max(land[N - 1])  # 바로 위에 코드가 똑같은 코드다. N - 1행에서의 최대값을 가지는 열 answer에 대입한다.
    # answer = max(land[N - 1][0], land[N - 1][1], land[N - 1][2], land[N - 1][3])

    return answer
