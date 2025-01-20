for _ in range(int(input())):
    s, n = input().split()
    n = int(n)
    if n >= 97: res = "A+"
    elif n >= 90: res = "A"
    elif n >= 87: res = "B+"
    elif n >= 80: res = "B"
    elif n >= 77: res = "C+"
    elif n >= 70: res = "C"
    elif n >= 67: res = "D+"
    elif n >= 60: res = "D"
    else: res = "F"
    print(s, res)
