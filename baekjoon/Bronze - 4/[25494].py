t = int(input())

while t > 0 :
    a, b, c = map(int, input().split())
    
    print(min(a, min(b, c)))
    
    t -= 1
