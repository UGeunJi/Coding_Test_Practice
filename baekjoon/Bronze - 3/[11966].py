n = int(input())
squares = [2 ** i for i in range(31)]

if n in squares:
    print(1)
else:
    print(0)
