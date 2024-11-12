a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180:
    print('Error')
elif a + b + c == 180 and a == 60 and b == 60 and c == 60:
    print('Equilateral')
elif a + b + c == 180 and a != b and b != c and c != a:
    print('Scalene')
else:
    print('Isosceles')
