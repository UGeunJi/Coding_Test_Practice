l = int(input())
li = [i for i in range(1, l + 1) if l % i == 0]

print(sum(li))
