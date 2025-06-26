n = int(input())
s = input()
c = [s.count(i) for i in "uospc"]

print(min(c))
