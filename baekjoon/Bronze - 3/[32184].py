a, b = map(int, input().split())
 
if a % 2 == 0 and b % 2 != 0:	
    print((b - a) // 2 + 2)
else:
    print((b - a) // 2 + 1)
