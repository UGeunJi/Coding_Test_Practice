s = list(map(int, input().split()))

if sum(s) >= 100:
    print('OK')
else:
    if s.index(min(s)) == 0:
        print('Soongsil')
    elif s.index(min(s)) == 1:
        print('Korea')
    elif s.index(min(s)) == 2:
        print('Hanyang')
