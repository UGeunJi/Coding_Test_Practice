for _ in range(int(input())) :
    G, C, E = map(int, input().split())
    cnt = (E - C) * [1, 3, 5][G - 1]
    print([cnt, 0][cnt <= 0])
