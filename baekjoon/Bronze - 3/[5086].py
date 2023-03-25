while True:
    a, b = map(int, input().split())
    
    if a == 0 and b == 0:
        break
    
    if a >= b and a % b == 0:
        print("multiple")
    elif a >= b and a % b != 0:
        print("neither")
    elif b % a == 0:
        print("factor")
              
