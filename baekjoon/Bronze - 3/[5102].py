while True :
    a, b = map(int, input().split())
    if a == b == 0: 
          break
    if a - b > 3: 
        print((a - b) // 2 - (a - b) % 2, (a - b) % 2)
    elif a - b == 3: 
        print(0, 1)
    elif a - b == 2:
        print(1, 0)
    else: 
        print(0, 0)
