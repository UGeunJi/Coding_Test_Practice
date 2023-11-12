chess = {
    "K": 0,
    "k": 0,
    "P": 1,
    "p": 1,
    "N": 3,
    "n": 3,
    "B": 3,
    "b": 3,
    "R": 5,
    "r": 5,
    "Q": 9,
    "q": 9,
}

white, black = 0, 0
for _ in range(8):
    pieces = input()
    for p in pieces:
        if p == ".":
            continue
        if p.isupper():
            white += chess[p]
        else:
            black += chess[p]

print(white - black)
