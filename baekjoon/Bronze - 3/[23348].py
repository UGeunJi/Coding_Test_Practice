score = list(map(int, input().split()))
n = int(input())
final = []

for _ in range(n):
    s = []
    for _ in range(3):
        a, b, c = map(int, input().split())
        s_temp = a * score[0] + b * score[1] + c * score[2]
        s.append(s_temp)
    final.append(sum(s))

print(max(final))
