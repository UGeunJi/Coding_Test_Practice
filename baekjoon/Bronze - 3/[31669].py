n, m = map(int, input().split())
school = [list(input()) for _ in range(n)]
home = list(map(list, zip(*school)))

result = 0
for i in range(len(home)):
    if home[i].count("X") == n:
        result = i + 1
        break

if result > 0:
    print(result)
else:
    print("ESCAPE FAILED")
