temp = []
for i in range(5):
    n = int(input())
    if n in temp:
        temp.remove(n)
    else:
        temp.append(n)
        
print(temp[0])
