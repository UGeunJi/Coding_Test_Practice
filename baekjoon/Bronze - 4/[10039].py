answer = 0
for i in range(5):
    num = int(input())
    if num <= 40:
        answer += 40
    else:
        answer += num
print(answer // 5)
