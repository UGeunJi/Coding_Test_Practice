N = int(input())
B = S = A = 0

for i in input():
    if i == "B":
        B += 1
    elif i == "S":
        S += 1
    elif i == "A":
        A += 1

if B == S and S == A and B == A:
    print("SCU")
else:
    if B == max(B, S, A):
        print("B", end="")
    if S == max(B, S, A):
        print("S", end="")
    if A == max(B, S, A):
        print("A", end="")
