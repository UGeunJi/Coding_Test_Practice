from math import pi

for _ in range(int(input())) :
    a, p1 = map(float, input().split())
    r, p2 = map(float, input().split())
    val1, val2 = a / p1, (pi * r ** 2) / p2
    
    print(["Slice of pizza", "Whole pizza"][val1 < val2])
