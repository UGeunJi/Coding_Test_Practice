n = int(input())
mirror = [input() for _ in range(n)]
k = int(input())
 
if k == 1:    # 원본 출력
    print(*mirror, sep='\n')
elif k == 2:    # 좌우 반전
    print(*[i[::-1] for i in mirror], sep='\n')
else:    # 상하 반전
    print(*mirror[::-1], sep='\n')
