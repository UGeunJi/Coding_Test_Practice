a, b, c = map(int, input().split())

temp = 0

if a >= 1000:
    temp = 1
else:
    print('Bad')
    
if temp == 1 and (b >= 8000 or c >= 260):
    temp += 1
    
if temp == 1:
    print('Good')
elif temp == 2:
    print('Very Good')
