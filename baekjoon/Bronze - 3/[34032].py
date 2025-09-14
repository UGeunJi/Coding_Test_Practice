n = int(input())
s = list(input())
h = n // 2
 
if n % 2 != 0:
    h += 1
 
if s.count("O") >= h:
    print("Yes")
else:
    print("No")
