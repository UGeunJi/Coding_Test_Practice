t = int(input())
 
for _ in range(t):
    n = int(input())
 
    if (n ** 0.5) % 1 == 0:
        print(1)
    else:
        print(0)
