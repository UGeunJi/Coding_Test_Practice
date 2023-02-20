s = input()

ss = ''
for i in s:
    if i.isalpha():
        if i.islower() and ord(i) + 13 >= 123:
            ss += chr(ord(i) - 13)
        elif i.isupper() and ord(i) + 13 >= 91:
            ss += chr(ord(i) - 13)
        else:
            ss += chr(ord(i) + 13)
    else:
        ss += i

print(ss)
