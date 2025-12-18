Q = int(input())
 
for _ in range(Q):
    a, b = map(int, input().split())
 
    if a < b:
        inner = b - a
        outer = 43 - (b - a)
    else:
        inner = 43 - (a - b)
        outer = a - b
 
    if inner < outer:
        print("Inner circle line")
    elif inner > outer:
        print("Outer circle line")
    else:
        print("Same")
