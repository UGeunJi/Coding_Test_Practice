l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
answer = []

an1 = l1[0] * 6 + l1[1] * 3 + l1[2] * 2 + l1[3] * 1 + l1[4] * 2
an2 = l2[0] * 6 + l2[1] * 3 + l2[2] * 2 + l2[3] * 1 + l2[4] * 2
answer.append(an1)
answer.append(an2)

print(*answer)
