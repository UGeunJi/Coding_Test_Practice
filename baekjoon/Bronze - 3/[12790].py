n = int(input())

for _ in range(n):
    hp, mp, att, de, hpp, mpp, attt, dee = map(int, input().split())
    
    hp += hpp
    mp += mpp
    att += attt
    de += dee
    
    if hp < 1:
        hp = 1
    if mp < 1:
        mp = 1
    if att < 0:
        att = 0
    
    hp *= 1
    mp *= 5
    att *= 2
    de *= 2
    
    print(hp + mp + att + de)
