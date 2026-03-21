score = 0

for i in range(9):
    if input() == 'Tiger':
        score += 1
    else:
        score -= 1

if score > 0:
    print('Tiger')
else:
    print('Lion')
