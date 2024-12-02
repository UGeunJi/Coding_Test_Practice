import sys
t = int(input())

for _ in range(t):
    a, b = map(int,sys.stdin.readline().split())
    BMI = b / ((a / 100) ** 2)
    
    if(a >= 204):
        print(4)
    elif(a >= 161):
        if(BMI >= 35 or BMI < 16):
            print(4)
        elif(BMI >= 20 and BMI < 25):
            print(1)
        elif(20 > BMI >= 18.5 or 30 > BMI >= 25):
            print(2)
        elif(18.5 > BMI >= 16.0 or 35 > BMI >= 30):
            print(3)
    elif(a >= 159):
        if(35 > BMI >= 16):
            print(3)
        else:
            print(4)
    elif(a >= 146):
        print(4)
    elif(a >= 140.1):
        print(5)
    else:
        print(6)
