li = list(map(int, input().split()))

if li[0] > 100 or li[1] > 100 or li[2] > 200 or li[3] > 200 or li[4] > 300 or li[5] > 300 or li[6] > 400 or li[7] > 400 or li[8] > 500:
    print('hacker')
elif sum(li) < 100:
    print('none')
else:
    print('draw')
