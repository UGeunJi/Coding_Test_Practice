t = int(input())

for i in range(t):
    c, f = map(int, input().split())
    print("You get {0} piece(s) and your dad gets {1} piece(s).".format(c // f, c % f))
