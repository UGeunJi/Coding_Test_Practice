str = input()
s = ''

for i in str:
    if i.isupper():
        s += i.lower()
    elif i.islower():
        s += i.upper()

print(s)
