from re import split

for _ in range(int(input())):
    s = input().replace(" ", "").upper()
    a = len(''.join(split("[AEIOU]+", s)))
    b = len(s) - a
    print(a, b)
