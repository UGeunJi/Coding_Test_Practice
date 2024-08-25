t = int(input())

for _ in range(t):
    l, r, s = map(int, input().split())
    L_Check, R_Check = s - l, r - s
    if L_Check < R_Check:
        print(L_Check * 2 + 1)
    else:
        print(R_Check * 2)
