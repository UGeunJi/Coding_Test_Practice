import sys

n = int(sys.stdin.readline())
score = 0
updated_score = 0

for i in range(n):
    score_l = list(map(int, sys.stdin.readline().split()))
    score1 = score_l[0:2]
    score2 = score_l[2:]
    score2.sort()
    
    updated_score += max(score1)
    updated_score += score2[-1] + score2[-2]
                 
    if updated_score > score:
        score = updated_score
        updated_score = 0
    else:
        updated_score = 0

print(score)
