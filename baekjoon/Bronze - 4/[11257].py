num = int(input())

for i in range(num):
    a, b, c, d = map(int, input().split())
    
    s = b + c + d
    if s < 55:
        print(f"{a} {s} FAIL")
    elif b / 35 < 0.3:
        print(f"{a} {s} FAIL")
    elif c / 25 < 0.3:
        print(f"{a} {s} FAIL")
    elif d / 40 < 0.3:
        print(f"{a} {s} FAIL")
    elif d / 40 >= 0.3 and c / 25 >= 0.3 and b / 35 >= 0.3:
        print(f"{a} {s} PASS")
