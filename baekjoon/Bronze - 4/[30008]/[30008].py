n, k = map(int, input().split())
grade = list(map(int, input().split()))
temp, ans = [], []

for i in range(k):
    temp.append(grade[i] * 100 // n)
    
for i in range(k):
    if 0 <= temp[i] <= 4:
        ans.append(1)
    elif 4 < temp[i] <= 11:
        ans.append(2)
    elif 11 < temp[i] <= 23:
        ans.append(3)
    elif 23 < temp[i] <= 40:
        ans.append(4)
    elif 40 < temp[i] <= 60:
        ans.append(5)
    elif 60 < temp[i] <= 77:
        ans.append(6)
    elif 77 < temp[i] <= 89:
        ans.append(7)
    elif 89< temp[i] <= 96:
        ans.append(8)
    elif 96 < temp[i] <= 100:
        ans.append(9)

print(*ans)
