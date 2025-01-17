s = input()
li = [1, 2, 3, 4]

for c in s:
    if c == 'A':
        li[0], li[1] = li[1], li[0]
    elif c == 'B':
        li[0], li[2] = li[2], li[0]
    elif c == 'C':
            li[0], li[3] = li[3], li[0]
    elif c == 'D':
            li[1], li[2] = li[2], li[1]
    elif c == 'E':
            li[1], li[3] = li[3], li[1]
    elif c == 'F':
            li[2], li[3] = li[3], li[2]
      
print(li.index(1) + 1)
print(li.index(4) + 1)
