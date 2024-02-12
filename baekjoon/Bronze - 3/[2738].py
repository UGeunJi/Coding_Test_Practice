x, y = map(int, input().split())
li = [x / y]

for _ in range(int(input())):
    x, y = map(int, input().split())
    li.append(x / y)
    
print("%.2f" % (min(li) * 1000))
