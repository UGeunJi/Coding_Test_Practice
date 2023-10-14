a = int(input())
b = int(input())

if a >= b:
    print('Congratulations, you are within the speed limit!')
else:
    if 1 <= (b - a) <= 20:
        print('You are speeding and your fine is $100.')
    elif 21 <= (b - a) <= 30:
        print('You are speeding and your fine is $270.')
    elif 31 <= (b - a):
        print('You are speeding and your fine is $500.')
