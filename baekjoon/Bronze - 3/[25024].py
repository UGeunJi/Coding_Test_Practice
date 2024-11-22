import sys

t = int(input())
a1 = [1,3,5,7,8,10,12]
a2 = [4,6,9,11]

for _ in range(t):
    A = "No"
    B = "No"
    a, b = map(int,sys.stdin.readline().split())
    if(a > 0 and a <= 12):
        if(a in a1 and b <= 31 and b > 0):
            A = "Yes"
        elif(a in a2 and b <= 30 and b > 0): 
            A = "Yes"
        elif(a == 2 and b <= 29 and b > 0):
            A = "Yes"
    if(a >= 0 and a <= 23):
        if(b <= 59):
            B = "Yes"
    
    print(B, A)
