line = input()
score = 1
total = 1

for i in range(1, len(line)):
    if line[i] > line[i - 1]:
        score += 1
    else:
        score = 1
    total += score

print(total)
