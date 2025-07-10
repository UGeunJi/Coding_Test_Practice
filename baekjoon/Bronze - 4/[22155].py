for _ in range(int(input())) :
    i, f = map(int, input().split())
    print(["No", "Yes"][i <= 1 and f <= 2 or i <= 2 and f <= 1])
