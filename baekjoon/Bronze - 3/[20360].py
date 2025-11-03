n = bin(int(input()))[2:]
for idx, i in enumerate(n[::-1], 0):
    if i == '1':
        print(idx, end=" ")
