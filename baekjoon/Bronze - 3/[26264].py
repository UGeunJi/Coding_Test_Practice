N = int(input())
a = input()
b = a.count('bigdata')
s = a.count('security')

if b > s :
    print('bigdata?')
elif b < s :
    print('security!')
else :
    print('bigdata? security!')
