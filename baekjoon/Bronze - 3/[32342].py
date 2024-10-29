q = int(input())

for _ in range(q):
    s = input()
    r = 0
    for i in range(len(s) - 2):
        if s[i:i + 3] == "WOW":
            r += 1

    print(r)
