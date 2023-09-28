n = input()

if '7' in n and int(n) % 7 == 0:
    print(3)
elif '7' in n and int(n) & 7 != 0:
    print(2)
elif int(n) % 7 == 0:
    print(1)
else:
    print(0)
